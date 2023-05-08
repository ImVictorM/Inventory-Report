from inventory_report.importer.importer import Importer
import xml.etree.ElementTree as ET


class XmlImporter(Importer):
    @classmethod
    def import_data(cls, file_path):
        if not file_path.endswith(".xml"):
            raise ValueError("Arquivo inválido")

        tree = ET.parse(file_path)
        dataset = tree.getroot()
        xml_to_list = []

        for record in dataset:
            item = {}
            for child in record:
                item[child.tag] = child.text

            xml_to_list.append(item)

        return xml_to_list
