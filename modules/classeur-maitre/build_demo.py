from __future__ import annotations

import argparse
from datetime import date
from pathlib import Path

from openpyxl import Workbook
from openpyxl.styles import Alignment, Font, PatternFill
from openpyxl.worksheet.table import Table, TableStyleInfo


def build(destination: Path) -> None:
    workbook = Workbook()
    workbook.properties.creator = "Textility"
    workbook.properties.lastModifiedBy = "Textility"
    readme = workbook.active
    readme.title = "LIRE"
    readme_rows = [
        ("Classeur fictif — prêts de matériel",),
        ("Démonstration Textility : toutes les personnes, dates et données sont fictives.",),
        ("Prets est le registre maître limité aux lignes de prêt de cet exemple; aucune réservation n’est représentée.",),
        ("Champs : Objet (désignation), Personne emprunteuse, Date de sortie, Retour prévu.",),
        ("La durée de conservation n’est pas décidée. Questions et décisions doivent rester distinctes du registre.",),
        ("build_demo.py génère ce classeur; export_markdown.py lit Prets et crée une projection Markdown.",),
        ("Droits : exemple sans données personnelles réelles; conserver et utiliser uniquement comme exercice.",),
        ("Limites : protection de feuille/classeur non activée; un XLSX généré n’est pas une recette Excel native.",),
        ("La projection est dérivée, non indépendante; exporte aussi les lignes masquées/filtrées.",),
    ]
    for row in readme_rows:
        readme.append(row)
    loans = workbook.create_sheet("Prets")
    loans.append(["Objet", "Personne emprunteuse", "Date de sortie", "Retour prévu"])
    loans.append(["DEMO-OBJ-A", "DEMO-A", date(2026, 1, 12), date(2026, 1, 19)])
    loans.append(["DEMO-OBJ-B", "DEMO-B", date(2026, 2, 3), date(2026, 2, 10)])
    loans.append(["DEMO-OBJ-C", "DEMO-C", date(2026, 3, 8), date(2026, 3, 15)])
    for row in loans.iter_rows(min_row=2, min_col=3, max_col=4):
        for cell in row:
            cell.number_format = "yyyy-mm-dd"
    table = Table(displayName="TablePrets", ref="A1:D4")
    table.tableStyleInfo = TableStyleInfo(name="TableStyleMedium2", showRowStripes=True, showColumnStripes=False)
    loans.add_table(table)
    loans.freeze_panes = "A2"

    journal = workbook.create_sheet("Journal")
    journal.append(["Trace", "Base SHA-256", "Delta", "Autorité/source", "Résultat/limites"])
    journal.freeze_panes = "A2"

    header_fill = PatternFill("solid", fgColor="D9E2F3")
    for sheet in workbook.worksheets:
        sheet.sheet_view.showGridLines = False
        sheet.sheet_properties.pageSetUpPr.fitToPage = True
        sheet.page_setup.orientation = "landscape"
        sheet.page_setup.fitToWidth = 1
        sheet.page_setup.fitToHeight = 1
        sheet.sheet_properties.pageSetUpPr.autoPageBreaks = False
        sheet.page_margins.left = 0.25
        sheet.page_margins.right = 0.25
        sheet.page_margins.top = 0.5
        sheet.page_margins.bottom = 0.5
        sheet.sheet_view.zoomScale = 90
        for cell in sheet[1]:
            cell.font = Font(name="Calibri", bold=True, color="000000")
            cell.fill = header_fill
            cell.alignment = Alignment(vertical="top", wrap_text=True)
        for row in sheet.iter_rows():
            for cell in row:
                cell.font = Font(name="Calibri", bold=(cell.row == 1), color="000000")
                cell.alignment = Alignment(vertical="top", wrap_text=True)
        sheet.sheet_format.defaultRowHeight = 30
    readme.column_dimensions["A"].width = 115
    readme.sheet_view.showGridLines = False
    loans.column_dimensions["A"].width = 24
    loans.column_dimensions["B"].width = 30
    loans.column_dimensions["C"].width = 18
    loans.column_dimensions["D"].width = 18
    for column, width in {"A": 24, "B": 20, "C": 24, "D": 28, "E": 38}.items():
        journal.column_dimensions[column].width = width

    with destination.open("xb") as stream:
        workbook.save(stream)


def main() -> int:
    parser = argparse.ArgumentParser(description="Génère le classeur fictif de démonstration.")
    parser.add_argument("destination", type=Path, help="Chemin de sortie explicite (doit être absent).")
    args = parser.parse_args()
    try:
        build(args.destination)
    except FileExistsError:
        parser.error(f"la destination existe déjà : {args.destination}")
    except OSError as exc:
        parser.error(f"impossible de créer le classeur : {exc}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
