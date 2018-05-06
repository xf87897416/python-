#_*_ coding:utf-8 _*_
#_author: "Administrator"
#date: 2017/11/3

import xml.etree.ElementTree as ET
new_xml = ET.Element("namelist")
name = ET.SubElement(new_xml,'name',attrib={'enrolled': 'yes'})
age = ET.SubElement(name,'age',attrib={'cheched':'no'})
sex = ET.SubElement(name,'sex')

name2 = ET.SubElement(new_xml,'name',attrib={'enrolled': 'no'})
age = ET.SubElement(name2,"age")
age.text = '19'

et = ET.ElementTree(new_xml)
et.write('test.xml',encoding='utf-8',xml_declaration=True)

ET.dump(new_xml)

















