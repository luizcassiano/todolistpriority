from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import unittest


#class NewVsitorTest(unittest.TestCase):

    #def setUp(self):
     #   self.browser = webdriver.Chrome(executable_path=r"C:\Others\chromedriver_win32\chromedriver.exe")

    #def tearDown(self):
    #    self.browser.quit()

    #    browser.get("http://localhost:8000")


from selenium import webdriver

browser = webdriver.Chrome(executable_path=r"C:\Others\chromedriver_win32\chromedriver.exe")
browser.get("http://localhost:8000")

assert 'worked successfully' in browser.title