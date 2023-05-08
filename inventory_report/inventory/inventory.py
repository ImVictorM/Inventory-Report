import csv
import json
import xml.etree.ElementTree as ET
from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport


class Inventory:
    @classmethod
    def csv_to_list(cls, file):
        reader = csv.DictReader(file)
        inventory = [row for row in reader]
        return inventory

    @classmethod
    def json_to_list(cls, file):
        inventory = json.load(file)
        return inventory

    @classmethod
    def xml_to_list(cls, file_path):
        tree = ET.parse(file_path)
        dataset = tree.getroot()
        xml_to_list = []

        for record in dataset:
            item = {}
            for child in record:
                item[child.tag] = child.text

            xml_to_list.append(item)

        return xml_to_list

    @classmethod
    def import_data(cls, file_path, report_type):
        with open(file_path) as file:
            inventory = []

            if file_path.endswith(".csv"):
                inventory = Inventory.csv_to_list(file)
            elif file_path.endswith(".json"):
                inventory = Inventory.json_to_list(file)
            else:
                # xml case
                inventory = Inventory.xml_to_list(file_path)

            if report_type == "simples":
                return SimpleReport.generate(inventory)
            else:
                # complete case
                return CompleteReport.generate(inventory)
