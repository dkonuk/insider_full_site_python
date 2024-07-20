from Pages.BaseFunctions import BaseFunctions
from Test_Data.test_Data import test_Data
from selenium.webdriver.common.by import By


class NavBarSolutionsPage(BaseFunctions):

    accept_cookies_button = (By.CSS_SELECTOR, "#wt-cli-accept-all-btn")
    navbar_customers = (By.XPATH, '//*[@id="navbarNavDropdown"]/ul[1]/li[4]')

    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(test_Data.url)

    def accept_cookies(self):
        try:
            self.click_element(self.accept_cookies_button)
        except:
            pass

    def nav_bar_customers(self):
        self.click_element(self.navbar_customers)