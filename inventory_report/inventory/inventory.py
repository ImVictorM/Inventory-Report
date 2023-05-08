import csv
from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport


class Inventory:
    @classmethod
    def import_data(cls, csv_path, report_type):
        with open(csv_path) as csv_file:
            reader = csv.DictReader(csv_file)
            inventory = [row for row in reader]
            if report_type == 'simples':
                return SimpleReport.generate(inventory)
            else:
                return CompleteReport.generate(inventory)


Inventory.import_data('inventory_report/data/inventory.csv', 'simples')
