from selenium import webdriver
from bs4 import BeautifulSoup
import unittest
import json

# tests need to import xml and get data and simulate input...

class APITest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()
        # waits a little to let browser respond
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.refresh()
        self.browser.quit()

    def test_read(self):
        """test general url returns json"""
        self.browser.get('http://localhost:8000/fenland/1/volunteer_id/1')
        soup = BeautifulSoup(self.browser.page_source)
        dict_from_soup = json.loads(soup.find('body').text)
        self.assertIn('Gillies', dict_from_soup['surname'])
        self.assertIn('David', dict_from_soup['forenames'])
        
    def test_input(self):
        pass


if __name__ == '__main__':
    unittest.main()
