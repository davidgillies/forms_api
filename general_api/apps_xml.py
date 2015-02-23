import glob
import ntpath
from cam_apps import Application


xml_files = glob.glob('U:/Data/forms_api/forms_api/xmlfiles/*.xml')

apps = {}

for xml_file in xml_files:
    xml_file_name = ntpath.split(xml_file)[1].split('.')[0].lower()
    xml_string = open(xml_file, 'r').read()
    apps[xml_file_name] = Application(xml_file_name, xml_string)
