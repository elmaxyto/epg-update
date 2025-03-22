import xml.etree.ElementTree as ET

# Carica le EPG
tree_main = ET.parse('epg.xml')
root_main = tree_main.getroot()

tree_pluto = ET.parse('pluto_tv_epg.xml')
root_pluto = tree_pluto.getroot()

# Unisci le EPG
for channel in root_pluto.findall('.//channel'):
    root_main.append(channel)

# Salva l'EPG unificata
tree_main.write('epg.xml', encoding='utf-8', xml_declaration=True)
