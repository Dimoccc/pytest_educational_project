import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

class BasePage():

    def __init__(self, browser, url):
        self.browser = browser
        self.url = url

    def open(self):
        self.browser.get(self.url)