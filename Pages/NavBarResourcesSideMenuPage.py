from Pages.BaseFunctions import BaseFunctions
from Test_Data.test_Data import test_Data
from selenium.webdriver.common.by import By

class NavBarResourcesSideMenuPage(BaseFunctions):

    accept_cookies_button = (By.CSS_SELECTOR, "#wt-cli-accept-all-btn")
    navbar_resources = (By.XPATH, '//*[@id="navbarNavDropdown"]/ul[1]/li[5]')
    navbar_resources_case_Studies = (By.CSS_SELECTOR, "#navbarNavDropdown > ul:nth-child(1) > li.nav-item.dropdown.show > div > div.new-menu-dropdown-layout-5-mid-container > a:nth-child(2)")
    navbar_resources_blog = (By.CSS_SELECTOR, "#navbarNavDropdown > ul:nth-child(1) > li.nav-item.dropdown.show > div > div.new-menu-dropdown-layout-5-mid-container > a:nth-child(3)")
    navbar_resources_webinars = (By.CSS_SELECTOR, "#navbarNavDropdown > ul:nth-child(1) > li.nav-item.dropdown.show > div > div.new-menu-dropdown-layout-5-mid-container > a:nth-child(4)")
    navbar_resources_reports = (By.CSS_SELECTOR, "#navbarNavDropdown > ul:nth-child(1) > li.nav-item.dropdown.show > div > div.new-menu-dropdown-layout-5-mid-container > a:nth-child(5)")
    navbar_resources_ebooks_guides = (By.CSS_SELECTOR, "#navbarNavDropdown > ul:nth-child(1) > li.nav-item.dropdown.show > div > div.new-menu-dropdown-layout-5-mid-container > a:nth-child(6)")
    navbar_resources_glossary = (By.CSS_SELECTOR, "#navbarNavDropdown > ul:nth-child(1) > li.nav-item.dropdown.show > div > div.new-menu-dropdown-layout-5-mid-container > a:nth-child(7)")


    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(test_Data.url)

    def accept_cookies(self):
        try:
            self.click_element(self.accept_cookies_button)
        except:
            pass

    def nav_bar_resources_case_Studies(self):
        self.click_navigation_bar_elements(self.navbar_resources, self.navbar_resources_case_Studies)

    def nav_bar_resources_blog(self):
        self.click_navigation_bar_elements(self.navbar_resources, self.navbar_resources_blog)

    def nav_bar_resources_webinars(self):
        self.click_navigation_bar_elements(self.navbar_resources, self.navbar_resources_webinars)

    def nav_bar_resources_reports(self):
        self.click_navigation_bar_elements(self.navbar_resources, self.navbar_resources_reports)

    def nav_bar_resources_ebooks_guides(self):
        self.click_navigation_bar_elements(self.navbar_resources, self.navbar_resources_ebooks_guides)

    def nav_bar_resources_glossary(self):
        self.click_navigation_bar_elements(self.navbar_resources, self.navbar_resources_glossary)
