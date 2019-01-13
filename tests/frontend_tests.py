from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import unittest


class FrontendTest(unittest.TestCase):

    def setUp(self):
        chrome_options = Options()
        # chrome_options.add_argument("--headless")
        self.driver = webdriver.Chrome(options=chrome_options)

    def tearDown(self):
        self.driver.close()

    def test_homepage(self):
        driver = self.driver
        driver.get("http://127.0.0.1:5000")
        self.assertIn("<h3>You want to see ..</h3>", driver.page_source)
        self.assertIn("Toots!", driver.title)

    def test_authors(self):
        driver = self.driver
        driver.get("http://127.0.0.1:5000/authors")
        self.assertIn('<span><a href="/author/0">Alice</a></span>', driver.page_source)
        self.assertIn("<span>zoot zoot!</span>", driver.page_source)

        charlie_links = driver.find_elements_by_link_text('Charlie')
        self.assertEqual(len(charlie_links), 13)

    def test_toots_by_author(self):
        driver = self.driver
        driver.get("http://127.0.0.1:5000/author/2")
        self.assertNotIn('<span><a href="/author/3">Dennis</a></span>', driver.page_source)
        self.assertNotIn("<span>doot noot!</span>", driver.page_source)
        self.assertIn("<span>zoot choot!</span>", driver.page_source)

        charlie_links = driver.find_elements_by_link_text('Charlie')
        self.assertEqual(len(charlie_links), 10)
