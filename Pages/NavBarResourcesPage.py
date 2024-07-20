from Pages.BaseFunctions import BaseFunctions
from Test_Data.test_Data import test_Data
from selenium.webdriver.common.by import By

class NavBarResourcesPage(BaseFunctions):

    accept_cookies_button = (By.CSS_SELECTOR, "#wt-cli-accept-all-btn")
    navbar_resources = (By.XPATH, '//*[@id="navbarNavDropdown"]/ul[1]/li[5]')
    navbar_resources_explore_insider = (By.CSS_SELECTOR, "#navbarNavDropdown > ul:nth-child(1) > li.nav-item.dropdown.show > div > div.menu-highlight-layout-5 > div.menu-highlight-layout-5-image-container > img")
    navbar_resources_take_tour = (By.CSS_SELECTOR, "#navbarNavDropdown > ul:nth-child(1) > li.nav-item.dropdown.show > div > div.new-menu-dropdown-layout-5-left-container > a:nth-child(2)")
    navbar_resources_cdp_explorer = (By.CSS_SELECTOR, "#navbarNavDropdown > ul:nth-child(1) > li.nav-item.dropdown.show > div > div.new-menu-dropdown-layout-5-left-container > a:nth-child(4)")
    navbar_whatsapp_explorer = (By.CSS_SELECTOR, "#navbarNavDropdown > ul:nth-child(1) > li.nav-item.dropdown.show > div > div.new-menu-dropdown-layout-5-left-container > a:nth-child(6)")
    navbar_sms_templates_library = (By.CSS_SELECTOR, "#navbarNavDropdown > ul:nth-child(1) > li.nav-item.dropdown.show > div > div.new-menu-dropdown-layout-5-left-container > a:nth-child(8)")
    navbar_productivity_calculator = (By.CSS_SELECTOR, "#navbarNavDropdown > ul:nth-child(1) > li:nth-child(5) > div > div.new-menu-dropdown-layout-5-left-container > a:nth-child(10)")



    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(test_Data.url)

    def accept_cookies(self):
        try:
            self.click_element(self.accept_cookies_button)
        except:
            pass

    def click_nav_bar_resources_explore_insider(self):
        self.click_navigation_bar_elements(self.navbar_resources, self.navbar_resources_explore_insider)
        self.previous_page()

    def click_nav_bar_resources_take_tour(self):
        self.click_navigation_bar_elements(self.navbar_resources, self.navbar_resources_take_tour)
        self.previous_page()

    def click_navbar_resources_cdp_explorer(self):
        self.click_navigation_bar_elements(self.navbar_resources, self.navbar_resources_cdp_explorer)
        self.previous_page()

    def click_navbar_whatsapp_explorer(self):
        self.click_navigation_bar_elements(self.navbar_resources, self.navbar_whatsapp_explorer)
        self.previous_page()

    def click_navbar_sms_templates_library(self):
        self.click_navigation_bar_elements(self.navbar_resources, self.navbar_sms_templates_library)
        self.previous_page()

    def click_navbar_productivity_calculator(self):
        self.click_navigation_bar_elements(self.navbar_resources, self.navbar_productivity_calculator)
        self.previous_page()