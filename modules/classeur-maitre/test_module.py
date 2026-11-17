from __future__ import annotations

import hashlib
import subprocess
import sys
import tempfile
import unittest
from datetime import date
from pathlib import Path

from openpyxl import load_workbook

MODULE = Path(__file__).resolve().parent


def build_source(path: Path) -> None:
    result = subprocess.run([sys.executable, str(MODULE / "build_demo.py"), str(path)], capture_output=True, text=True)
    if result.returncode:
        raise AssertionError(result.stderr)


class DemoModuleTests(unittest.TestCase):
    def test_demo_workbook_generates_and_exports_without_changing_source(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            tmp_path = Path(directory)
            source = tmp_path / "maitre-prets-demo.xlsx"
            projection = tmp_path / "prets-generes.md"
            build_source(source)
            before = source.read_bytes()
            digest = hashlib.sha256(before).hexdigest()
            workbook = load_workbook(source, data_only=False)
            self.assertEqual(workbook.sheetnames, ["LIRE", "Prets", "Journal"])
            sheet = workbook["Prets"]
            self.assertEqual([sheet.cell(1, col).value for col in range(1, 5)], [
                "Objet", "Personne emprunteuse", "Date de sortie", "Retour prévu"
            ])
            self.assertEqual((sheet.max_row, sheet.max_column), (4, 4))
            self.assertTrue(all(sheet.cell(row, 1).value.startswith("DEMO-") for row in range(2, 5)))
            self.assertEqual(sheet["C2"].value.date().isoformat(), "2026-01-12")
            result = subprocess.run(
                [sys.executable, str(MODULE / "export_markdown.py"), str(source), str(projection)],
                capture_output=True, text=True,
            )
            self.assertEqual(result.returncode, 0, result.stderr)
            text = projection.read_text(encoding="utf-8")
            self.assertIn(digest, text)
            self.assertIn("Objet", text)
            self.assertIn("DEMO-", text)
            self.assertEqual(source.read_bytes(), before)

    def test_formula_in_any_sheet_is_rejected_before_destination_creation(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            source = Path(directory) / "source.xlsx"
            destination = Path(directory) / "result.md"
            build_source(source)
            workbook = load_workbook(source)
            workbook["LIRE"]["A1"] = "=1+1"
            workbook.save(source)
            result = subprocess.run(
                [sys.executable, str(MODULE / "export_markdown.py"), str(source), str(destination)],
                capture_output=True, text=True,
            )
            self.assertEqual(result.returncode, 2)
            self.assertIn("formule", result.stderr)
            self.assertFalse(destination.exists())

    def test_extra_header_is_rejected_before_destination_creation(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            source = Path(directory) / "source.xlsx"
            destination = Path(directory) / "result.md"
            build_source(source)
            workbook = load_workbook(source)
            workbook["Prets"]["E1"] = "Champ inattendu"
            workbook.save(source)
            result = subprocess.run(
                [sys.executable, str(MODULE / "export_markdown.py"), str(source), str(destination)],
                capture_output=True, text=True,
            )
            self.assertEqual(result.returncode, 2)
            self.assertIn("supplémentaire", result.stderr)
            self.assertFalse(destination.exists())

    def test_existing_output_is_never_overwritten(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            source = Path(directory) / "source.xlsx"
            build_source(source)
            expected = source.read_bytes()
            build_again = subprocess.run(
                [sys.executable, str(MODULE / "build_demo.py"), str(source)],
                capture_output=True, text=True,
            )
            self.assertEqual(build_again.returncode, 2)
            self.assertEqual(source.read_bytes(), expected)
            destination = Path(directory) / "result.md"
            destination.write_text("keep this", encoding="utf-8")
            exported = subprocess.run(
                [sys.executable, str(MODULE / "export_markdown.py"), str(source), str(destination)],
                capture_output=True, text=True,
            )
            self.assertEqual(exported.returncode, 2)
            self.assertEqual(destination.read_text(encoding="utf-8"), "keep this")

    def test_markdown_escapes_html_pipes_backslashes_and_line_breaks(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            source = Path(directory) / "source.xlsx"
            destination = Path(directory) / "result.md"
            build_source(source)
            workbook = load_workbook(source)
            workbook["Prets"]["A2"] = "A|B\\C\n<tag>"
            workbook.save(source)
            result = subprocess.run(
                [sys.executable, str(MODULE / "export_markdown.py"), str(source), str(destination)],
                capture_output=True, text=True,
            )
            self.assertEqual(result.returncode, 0, result.stderr)
            self.assertIn("A\\|B\\\\C<br>&lt;tag&gt;", destination.read_text(encoding="utf-8"))


    def test_provenance_and_open_question_are_visible(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            source = Path(directory) / "source.xlsx"
            destination = Path(directory) / "result.md"
            build_source(source)
            result = subprocess.run(
                [sys.executable, str(MODULE / "export_markdown.py"), str(source), str(destination)],
                capture_output=True, text=True,
            )
            self.assertEqual(result.returncode, 0, result.stderr)
            visible = "\n".join(line for line in destination.read_text(encoding="utf-8").splitlines() if not line.startswith("<!--"))
            self.assertIn("> **Projection générée", visible)
            self.assertIn("> **Source SHA-256 :**", visible)
            self.assertIn(hashlib.sha256(source.read_bytes()).hexdigest(), visible)
            self.assertIn("> **Conservation :** non décidée.", visible)


    def test_source_cannot_be_its_own_destination(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            source = Path(directory) / "source.xlsx"
            build_source(source)
            before = source.read_bytes()
            result = subprocess.run([sys.executable, str(MODULE / "export_markdown.py"), str(source), str(source)], capture_output=True, text=True)
            self.assertEqual(result.returncode, 2)
            self.assertEqual(source.read_bytes(), before)

    def test_invalid_data_is_refused_without_creating_a_view(self) -> None:
        cases = [("missing", "B2", None), ("extra", "E2", "extra"), ("text_date", "C2", "2026-01-12"), ("early_return", "D2", date(2025, 1, 1))]
        for name, address, value in cases:
            with self.subTest(name=name), tempfile.TemporaryDirectory() as directory:
                source = Path(directory) / "source.xlsx"
                destination = Path(directory) / "result.md"
                build_source(source)
                workbook = load_workbook(source)
                workbook["Prets"][address].value = value
                workbook.save(source)
                workbook.close()
                before = source.read_bytes()
                result = subprocess.run([sys.executable, str(MODULE / "export_markdown.py"), str(source), str(destination)], capture_output=True, text=True)
                self.assertEqual(result.returncode, 2, result.stderr)
                self.assertFalse(destination.exists())
                self.assertEqual(source.read_bytes(), before)

    def test_replay_includes_hidden_rows_and_repeated_object_names(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            source = Path(directory) / "source.xlsx"
            build_source(source)
            workbook = load_workbook(source)
            workbook["Prets"].row_dimensions[3].hidden = True
            workbook["Prets"]["A3"] = workbook["Prets"]["A2"].value
            workbook.save(source)
            workbook.close()
            before = source.read_bytes()
            outputs = [Path(directory) / "one.md", Path(directory) / "two.md"]
            for output in outputs:
                result = subprocess.run([sys.executable, str(MODULE / "export_markdown.py"), str(source), str(output)], capture_output=True, text=True)
                self.assertEqual(result.returncode, 0, result.stderr)
            self.assertEqual(outputs[0].read_bytes(), outputs[1].read_bytes())
            self.assertIn("DEMO-B", outputs[0].read_text(encoding="utf-8"))
            self.assertEqual(outputs[0].read_text(encoding="utf-8").count("| DEMO-OBJ-A |"), 2)
            self.assertEqual(source.read_bytes(), before)


if __name__ == "__main__":
    unittest.main()
