from Pages.BaseFunctions import BaseFunctions
from Test_Data.test_Data import test_Data
from selenium.webdriver.common.by import By


class NavBarSolutionsPage(BaseFunctions):

    accept_cookies_button = (By.CSS_SELECTOR, "#wt-cli-accept-all-btn")
    navbar_solutions = (By.XPATH, '//*[@id="navbarNavDropdown"]/ul[1]/li[3]')
    navbar_optimize_customer_acquisition = (By.CSS_SELECTOR, "#navbarNavDropdown > ul:nth-child(1) > li.nav-item.dropdown.show > div > div.new-menu-dropdown-layout-3-left-container > a:nth-child(2)")
    navbar_solutions_increase_customer_engagement = (By.CSS_SELECTOR, "#navbarNavDropdown > ul:nth-child(1) > li.nav-item.dropdown.show > div > div.new-menu-dropdown-layout-3-left-container > a:nth-child(4)")
    navbar_solutions_reduce_customer_churn = (By.CSS_SELECTOR, "#navbarNavDropdown > ul:nth-child(1) > li.nav-item.dropdown.show > div > div.new-menu-dropdown-layout-3-left-container > a:nth-child(6)")


    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(test_Data.url)

    def accept_cookies(self):
        try:
            self.click_element(self.accept_cookies_button)
        except:
            pass

    def nav_bar_solutions(self):
        self.click_navigation_bar_elements(self.navbar_solutions, self.navbar_optimize_customer_acquisition)

    def nav_bar_solutions_increase_customer_engagement(self):
        self.click_navigation_bar_elements(self.navbar_solutions, self.navbar_solutions_increase_customer_engagement)

    def nav_bar_solutions_reduce_customer_churn(self):
        self.click_navigation_bar_elements(self.navbar_solutions, self.navbar_solutions_reduce_customer_churn)




