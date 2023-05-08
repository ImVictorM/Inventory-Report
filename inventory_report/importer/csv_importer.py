from inventory_report.importer.importer import Importer
import csv


class CsvImporter(Importer):
    @classmethod
    def import_data(cls, file_path):
        if not file_path.endswith(".csv"):
            raise ValueError("Arquivo inválido")

        with open(file_path) as csv_file:
            inventory = []
            reader = csv.DictReader(csv_file)
            inventory = [row for row in reader]
            return inventory
