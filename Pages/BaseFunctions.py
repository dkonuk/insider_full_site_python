from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
import time

class BaseFunctions:

    def __init__(self, driver):
        self.driver = driver

    def find_element(self, element):
        return WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(element))

    def click_element(self, element):
        self.find_element(element).click()

    def click_navigation_bar_elements(self, nav_bar_menu, nav_bar_sub_menu):
        WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(nav_bar_menu)).click()
        time.sleep(1)
        WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(nav_bar_sub_menu)).click()

    def previous_page(self):
        self.driver.back()
