import csv
import json
import xml.etree.ElementTree as ET
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
            else:
                # xml case
                tree = ET.parse(file_path)
                dataset = tree.getroot()
                xml_to_list = []

                for record in dataset:
                    item = {}
                    for child in record:
                        item[child.tag] = child.text

                    xml_to_list.append(item)

                inventory = xml_to_list

            if report_type == "simples":
                return SimpleReport.generate(inventory)
            else:
                return CompleteReport.generate(inventory)
