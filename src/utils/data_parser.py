thonimport json
import csv

def parse_json_to_dict(filename):
    with open(filename, 'r') as json_file:
        data = json.load(json_file)
    return data

def parse_csv_to_dict(filename):
    with open(filename, 'r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        return [row for row in csv_reader]

def parse_xml_to_dict(filename):
    from xml.etree import ElementTree as ET
    tree = ET.parse(filename)
    root = tree.getroot()
    return parse_xml_element(root)

def parse_xml_element(element):
    parsed_data = {}
    for child in element:
        parsed_data[child.tag] = child.text
    return parsed_data