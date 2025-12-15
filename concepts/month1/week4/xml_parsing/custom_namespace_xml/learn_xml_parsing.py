import xml.etree.cElementTree as ET

from inspect import getmembers, isclass, isfunction

tree = ET.parse("Books.xml")
root=tree.getroot()