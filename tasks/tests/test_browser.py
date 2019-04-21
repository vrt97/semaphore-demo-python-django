"""
    Unit Test file for views
"""
from os import sep

from django.test import TestCase

from selenium import webdriver

from pydjango_ci_integration.settings import BASE_DIR, SITE_URL


class TaskListViewTest(TestCase):
    """
    Test View class
    """
    # # Browser Integration testing with Selenium
    def test_chrome_site_homepage(self):
        chrome_driver_path = BASE_DIR + sep + 'chromedriver' + sep + 'chromedriver'
        browser = webdriver.Chrome(executable_path=chrome_driver_path)
        browser.get(SITE_URL)
        self.assertIn('Semaphore', browser.title)
        browser.close()
