from __future__ import annotations

import argparse
import hashlib
import html
import sys
from datetime import date, datetime
from io import BytesIO
from pathlib import Path

from openpyxl import load_workbook

EXPECTED_SHEETS = ["LIRE", "Prets", "Journal"]
HEADERS = ["Objet", "Personne emprunteuse", "Date de sortie", "Retour prévu"]


class ExportError(ValueError):
    pass


def _cell_text(value: object) -> str:
    if isinstance(value, datetime):
        value = value.date()
    if isinstance(value, date):
        text = value.isoformat()
    else:
        text = str(value)
    text = html.escape(text, quote=False)
    return text.replace("\\", "\\\\").replace("|", "\\|").replace("\r\n", "<br>").replace("\r", "<br>").replace("\n", "<br>")


def _rows_from_snapshot(snapshot: bytes) -> list[list[object]]:
    try:
        workbook = load_workbook(BytesIO(snapshot), read_only=True, data_only=False, keep_links=False)
    except Exception as exc:
        raise ExportError(f"classeur XLSX illisible : {exc}") from exc
    try:
        if workbook.sheetnames != EXPECTED_SHEETS:
            raise ExportError("les onglets attendus sont exactement LIRE, Prets, Journal")
        for candidate in workbook.worksheets:
            for row_number, row in enumerate(candidate.iter_rows(), start=1):
                if any(cell.data_type == "f" for cell in row):
                    raise ExportError(f"formule interdite dans {candidate.title}, ligne {row_number}")
        sheet = workbook["Prets"]
        iterator = sheet.iter_rows()
        first = next(iterator, ())
        if [cell.value for cell in first[:4]] != HEADERS or len(first) < 4:
            raise ExportError("les quatre en-têtes de Prets sont absents ou incorrects")
        if any(cell.value is not None for cell in first[4:]):
            raise ExportError("colonne supplémentaire dans les en-têtes de Prets")
        rows: list[list[object]] = []
        for row_number, cells in enumerate(iterator, start=2):
            values = [cell.value for cell in cells]
            if all(value is None for value in values):
                continue
            if any(value is not None for value in values[4:]):
                raise ExportError(f"colonne supplémentaire non vide à la ligne {row_number}")
            values = values[:4]
            if any(value is None or (isinstance(value, str) and not value.strip()) for value in values):
                raise ExportError(f"champ absent à la ligne {row_number}")
            if any(isinstance(value, str) and value.startswith("=") for value in values):
                raise ExportError(f"formule interdite à la ligne {row_number}")
            start, due = values[2], values[3]
            if not isinstance(start, (date, datetime)) or not isinstance(due, (date, datetime)):
                raise ExportError(f"dates Excel réelles requises à la ligne {row_number}")
            if due < start:
                raise ExportError(f"retour prévu antérieur à la sortie à la ligne {row_number}")
            rows.append(values)
        return rows
    finally:
        workbook.close()


def render_markdown(snapshot: bytes) -> str:
    digest = hashlib.sha256(snapshot).hexdigest()
    rows = _rows_from_snapshot(snapshot)
    lines = [
        "> **Projection générée — démonstration fictive.** Cette vue n’est pas une source indépendante ; corriger le maître puis régénérer.",
        f"> **Source SHA-256 :** `{digest}`",
        "> **Conservation :** non décidée. Les lignes masquées ou filtrées sont incluses.",
        "",
        "# Projection des prêts (démonstration fictive)",
        "",
        "| Objet | Personne emprunteuse | Date de sortie | Retour prévu |",
        "| --- | --- | --- | --- |",
    ]
    for row in rows:
        lines.append("| " + " | ".join(_cell_text(value) for value in row) + " |")
    return "\n".join(lines) + "\n"


def exporter(source: Path, destination: Path) -> None:
    source, destination = Path(source), Path(destination)
    if source.resolve() == destination.resolve():
        raise ExportError("source et destination doivent être différentes")
    snapshot = source.read_bytes()
    markdown = render_markdown(snapshot)
    with destination.open("x", encoding="utf-8", newline="\n") as stream:
        stream.write(markdown)


def main() -> int:
    parser = argparse.ArgumentParser(description="Projection Markdown en lecture seule du registre Prets.")
    parser.add_argument("source", type=Path)
    parser.add_argument("destination", type=Path)
    args = parser.parse_args()
    try:
        exporter(args.source, args.destination)
    except (OSError, ExportError) as exc:
        print(f"export_markdown.py: {exc}", file=sys.stderr)
        return 2
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
