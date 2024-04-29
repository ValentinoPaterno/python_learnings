"""
XML is another structured data format which looks like HTML. 
In XML the tags are not predefined. The first line is an XML declaration. 
The person tag is the root of the XML. The person has a gender attribute. 
Example:XML
"""
import xml.etree.ElementTree as ET
tree = ET.parse('./18_file_handling/xml_example.xml')
root = tree.getroot()
print('Root tag:', root.tag)
print('Attribute:', root.attrib)
for child in root:
    print('field: ', child.tag)
