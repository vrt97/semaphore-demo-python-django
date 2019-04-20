"""
    Unit Test file for views
"""
from django.test import TestCase

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from pydjango_ci_integration.settings import SITE_URL


class TaskListViewTest(TestCase):
    """
    Test View class
    """
    # # Browser Integration testing with Selenium
    def test_chrome_site_homepage(self):
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        browser = webdriver.Chrome(chrome_options=chrome_options)
        browser.get(SITE_URL)
        self.assertIn('Semaphore', browser.title)
        browser.close()
