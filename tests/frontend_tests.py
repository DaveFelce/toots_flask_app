from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import unittest


class FrontendTest(unittest.TestCase):

    def setUp(self):
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        self.driver = webdriver.Chrome(chrome_options=chrome_options)

    def tearDown(self):
        self.driver.close()

    def test_homepage(self):
        driver = self.driver
        driver.get("http://127.0.0.1:5000")
        self.assertIn("<h3>Here they are</h3>", driver.page_source)
        self.assertIn("Toots!", driver.title)

