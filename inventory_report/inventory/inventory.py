import csv
import json
from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport


class Inventory:
    @classmethod
    def import_data(cls, file_path, report_type):
        with open(file_path) as file:
            inventory = []

            if file_path.endswith(".csv"):
                reader = csv.DictReader(file)
                inventory = [row for row in reader]
            elif file_path.endswith(".json"):
                inventory = json.load(file)

            if report_type == "simples":
                return SimpleReport.generate(inventory)
            else:
                return CompleteReport.generate(inventory)


Inventory.import_data("inventory_report/data/inventory.json", "simples")
