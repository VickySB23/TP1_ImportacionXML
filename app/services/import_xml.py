import xml.etree.ElementTree as ET

def import_xml_to_db(model_class, xml_path, session):
    tree = ET.parse(xml_path)
    root = tree.getroot()
    count = 0
    for node in root:
        obj = model_class.from_xml_node(node)
        session.merge(obj)  # merge evita duplicados por id
        count += 1
    session.commit()
    return count