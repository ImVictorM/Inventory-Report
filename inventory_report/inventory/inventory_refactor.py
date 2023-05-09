from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport
from inventory_report.importer.importer import Importer
from inventory_report.reports.report import Report
from inventory_report.inventory.inventory_iterator import InventoryIterator
from collections.abc import Iterable


class InventoryRefactor(Iterable):
    REPORT_TYPE_MAP = {
        "simples": SimpleReport,
        "completo": CompleteReport,
    }

    def __init__(self, importer: Importer) -> None:
        self.importer = importer
        self.data = []

    def import_data(self, file_path, report_type):
        inventory = self.importer.import_data(file_path)
        self.data.extend(inventory)
        report: Report = self.REPORT_TYPE_MAP.get(report_type)

        return report.generate(self.data)

    def __iter__(self):
        return InventoryIterator(self.data)
