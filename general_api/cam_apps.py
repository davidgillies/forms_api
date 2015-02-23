from lxml import objectify
import sqlsoup


# get this data from somewhere



class Application(object):
    def __init__(self, name, xml):
        self.name = name
        self.xml = xml
        self.xml_object = objectify.fromstring(self.xml)
        # self.variable_mapping
        # self.dbs get dbs from xml or somewhere
        self.db = sqlsoup.SQLSoup('mysql+pymysql://david:david@localhost:3306/sm_play')
        
# Need the variable names for each section

    def get_table_name(self):
        return 'volunteers'
    
    def get_section(self, section_number):
        return self.xml_object.section[int(section_number)]
        
    def get_data(self, section_number, id_variable, id_variable_value):
        section = self.get_section(section_number)
        self.db.table = self.db.entity(self.get_table_name())
        data = self.db.table.get(int(id_variable_value)).__dict__
        data.pop('_sa_instance_state')
        return data
        
    