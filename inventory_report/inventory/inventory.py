from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport
from inventory_report.importer.csv_importer import CsvImporter
from inventory_report.importer.json_importer import JsonImporter
from inventory_report.importer.xml_importer import XmlImporter
from inventory_report.importer.importer import Importer
from inventory_report.reports.report import Report


class Inventory:
    FILE_TYPE_IMPORTER_MAP = {
        ".csv": CsvImporter,
        ".json": JsonImporter,
        ".xml": XmlImporter,
    }

    REPORT_TYPE_MAP = {
        "simples": SimpleReport,
        "completo": CompleteReport,
    }

    @classmethod
    def import_data(cls, file_path, report_type):
        file_extension = file_path[file_path.rfind("."):]
        importer: Importer = cls.FILE_TYPE_IMPORTER_MAP.get(file_extension)

        inventory = importer.import_data(file_path)
        report: Report = cls.REPORT_TYPE_MAP.get(report_type)

        return report.generate(inventory)
