from selenium import webdriver
import unittest


class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()
        # waits a little to let browser respond
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.refresh()
        self.browser.quit()

    def test_general_url_works(self):
        self.browser.get('http://localhost:8000/bladebla')
        self.assertIn('bladebla', self.browser.title)


if __name__ == '__main__':
    unittest.main()
