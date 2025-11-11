thonimport json
import csv
import os

def export_data_to_json(data, path='data/output.json'):
    with open(path, 'w') as json_file:
        json.dump(data, json_file, indent=4)

def export_data_to_csv(data, path='data/output.csv'):
    if data:
        keys = data[0].keys()
        with open(path, 'w', newline='') as output_file:
            dict_writer = csv.DictWriter(output_file, fieldnames=keys)
            dict_writer.writeheader()
            dict_writer.writerows(data)

def export_data_to_xml(data, path='data/output.xml'):
    import dicttoxml
    xml_data = dicttoxml.dicttoxml(data)
    with open(path, 'wb') as xml_file:
        xml_file.write(xml_data)