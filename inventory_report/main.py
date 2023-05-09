import sys
from inventory_report.importer.csv_importer import CsvImporter
from inventory_report.importer.importer import Importer
from inventory_report.importer.json_importer import JsonImporter
from inventory_report.importer.xml_importer import XmlImporter
from inventory_report.inventory.inventory_refactor import InventoryRefactor


def main():
    if len(sys.argv) != 3:
        sys.stderr.write("Verifique os argumentos\n")
    else:
        FILE_TYPE_IMPORTER_MAP = {
            ".csv": CsvImporter,
            ".json": JsonImporter,
            ".xml": XmlImporter,
        }
        _, file_path, report_type = sys.argv
        file_extension = file_path[file_path.rfind("."):]
        importer: Importer = FILE_TYPE_IMPORTER_MAP.get(file_extension)

        report = InventoryRefactor(importer).import_data(
            file_path, report_type
        )

        sys.stdout.write(report)
