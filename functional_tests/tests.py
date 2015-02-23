from selenium import webdriver
from bs4 import BeautifulSoup
import unittest
import json



class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()
        # waits a little to let browser respond
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.refresh()
        self.browser.quit()

    def test_general_url_works(self):
        self.browser.get('http://localhost:8000/bladebla/etc/')
        soup = BeautifulSoup(self.browser.page_source)
        dict_from_soup = json.loads(soup.find('body').text)
        self.assertIn('bladebla', dict_from_soup['bladebla'])
        self.assertIn('etc', dict_from_soup['etc'])


if __name__ == '__main__':
    unittest.main()
