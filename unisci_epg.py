import xml.etree.ElementTree as ET

# Carica le EPG
tree_main = ET.parse('epg.xml')
root_main = tree_main.getroot()

tree_pluto = ET.parse('pluto_tv_epg.xml')
root_pluto = tree_pluto.getroot()

# Unisci i canali
for channel in root_pluto.findall('.//channel'):
    root_main.append(channel)

# Unisci i programme
for programme in root_pluto.findall('.//programme'):
    root_main.append(programme)

# Salva l'EPG unificata
tree_main.write('epg.xml', encoding='utf-8', xml_declaration=True)
