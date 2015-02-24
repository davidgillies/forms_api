from lxml import objectify
import sqlsoup
import simplejson


class Application(object):
    def __init__(self, name, xml):
        self.name = name
        self.xml = xml
        self.xml_object = objectify.fromstring(self.xml)
        # self.variable_mappings
        # self.dbs get dbs from xml or somewhere
        self.db = sqlsoup.SQLSoup('mysql+pymysql://david:david@localhost:3306/sm_play')

# Need the variable names for each section
# test with alternative db, sqlite.
# Any data I'd like to save to normal django models?

    def get_data(self, section_number, id_variable, id_variable_value):
        # note that if this GET requires html you'll need to check the variables
        # Have a is_dynamic() flag for a section to test
        self.db.table = self.db.entity(self.get_table_name())
        data = self.db.table.get(int(id_variable_value)).__dict__
        data.pop('_sa_instance_state')
        return data

    def insert_data(self, section_number, id_variable, id_variable_value, body):
        self.db.table = self.db.entity(self.get_table_name())
        json_dict = simplejson.JSONDecoder().decode(body)
        data = self.db.table.insert(**json_dict).__dict__
        data.pop('_sa_instance_state')
        self.db.commit()
        return data

    def update_data(self, section_number, id_variable, id_variable_value, body):
        self.db.table = self.db.entity(self.get_table_name())
        json_dict = simplejson.JSONDecoder().decode(body)
        # problem: can't put a variable into this filter_by must be a 
        # database column name
        data = self.db.table.filter_by(id=int(id_variable_value)).update(json_dict)
        data = json_dict
        self.db.commit()
        return data

    def delete_data(self, section_number, id_variable, id_variable_value):
        self.db.table = self.db.entity(self.get_table_name())
        instance = self.db.table.get(int(id_variable_value))
        self.db.delete(instance)
        self.db.commit()
        return

    def get_table_name(self):
        return 'volunteers'

    def is_dynamic(self, section):
        # test if section has a dynamic variable
        return False

    def get_section(self, section_number):
        return self.xml_object.section[int(section_number)]
