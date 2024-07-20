from Pages.BaseFunctions import BaseFunctions
from Test_Data.test_Data import test_Data
from selenium.webdriver.common.by import By

class HomePage(BaseFunctions):
    accept_cookies_button = (By.CSS_SELECTOR, "#wt-cli-accept-all-btn")
    why_insider_link = (By.XPATH, '//*[@id="navbarDropdownMenuLink"]')
    why_insider_insider_difference = (By.CSS_SELECTOR, "a[href='https://useinsider.com/why-insider']")
    why_insider_compare_vendors = (By.CSS_SELECTOR, "#navbarNavDropdown > ul:nth-child(1) > li.nav-item.dropdown.show > div > div.menu-container > a:nth-child(2)")
    why_insider_switch_to_insider = (By.CSS_SELECTOR, "#navbarNavDropdown > ul:nth-child(1) > li.nav-item.dropdown.show > div > div.menu-container > a:nth-child(3)")
    nav_bar_platform = (By.XPATH, '//*[@id="navbarNavDropdown"]/ul[1]/li[2]')
    nav_Bar_platform_overview = (By.CSS_SELECTOR, "#navbarNavDropdown > ul:nth-child(1) > li.nav-item.dropdown.show > div > div.new-menu-dropdown-layout-2-left-container > a.dropdown-main")
    nav_bar_platform_customer_data_management = (By.CSS_SELECTOR, ".new-menu-dropdown-layout-2-left-container > a:nth-child(3)")
    nav_bar_platform_customer_profiles = (By.XPATH, '//*[@id="navbarNavDropdown"]/ul[1]/li[2]/div/div[1]/a[3]')
    nav_bar_platform_predict_behavior = (By.CSS_SELECTOR, "#navbarNavDropdown > ul:nth-child(1) > li.nav-item.dropdown.show > div > div.new-menu-dropdown-layout-2-left-container > a:nth-child(5)")
    nav_bar_platform_personalization = (By.CSS_SELECTOR, "#navbarNavDropdown > ul:nth-child(1) > li.nav-item.dropdown.show > div > div.new-menu-dropdown-layout-2-left-container > a:nth-child(8)")
    nav_bar_platform_recommendations = (By.CSS_SELECTOR, "#navbarNavDropdown > ul:nth-child(1) > li.nav-item.dropdown.show > div > div.new-menu-dropdown-layout-2-left-container > a:nth-child(9)")
    nav_bar_platform_cdm_audience_segmengtation = (By.CSS_SELECTOR, "#navbarNavDropdown > ul:nth-child(1) > li.nav-item.dropdown.show > div > div.new-menu-dropdown-layout-2-left-container > a:nth-child(6)")
    nav_bar_platform_cdm_integrations = (By.CSS_SELECTOR, "#navbarNavDropdown > ul:nth-child(1) > li.nav-item.dropdown.show > div > div.new-menu-dropdown-layout-2-left-container > a:nth-child(7)")
    nav_bar_platform_personalization_vsd = (By.CSS_SELECTOR, "#navbarNavDropdown > ul:nth-child(1) > li.nav-item.dropdown.show > div > div.new-menu-dropdown-layout-2-left-container > a:nth-child(10)")
    nav_Bar_platform_personalization_pre_built = (By.CSS_SELECTOR, "#navbarNavDropdown > ul:nth-child(1) > li.nav-item.dropdown.show > div > div.new-menu-dropdown-layout-2-left-container > a:nth-child(11)")
    nav_bar_platform_personalization_site_search = (By.CSS_SELECTOR, "#navbarNavDropdown > ul:nth-child(1) > li.nav-item.dropdown.show > div > div.new-menu-dropdown-layout-2-left-container > a:nth-child(12)")
    nav_bar_platform_personalization_ab_Testing = (By.CSS_SELECTOR, "#navbarNavDropdown > ul:nth-child(1) > li.nav-item.dropdown.show > div > div.new-menu-dropdown-layout-2-left-container > a:nth-child(13)")
    nav_bar_platform_journey_orchestration = (By.CSS_SELECTOR, "#navbarNavDropdown > ul:nth-child(1) > li.nav-item.dropdown.show > div > div.new-menu-dropdown-layout-2-left-container > a:nth-child(14)")
    nav_bar_platform_insight_analytics = (By.CSS_SELECTOR, "#navbarNavDropdown > ul:nth-child(1) > li.nav-item.dropdown.show > div > div.new-menu-dropdown-layout-2-left-container > a:nth-child(15)")
    nav_bar_platform_behavorial_analytics = (By.CSS_SELECTOR, "#navbarNavDropdown > ul:nth-child(1) > li.nav-item.dropdown.show > div > div.new-menu-dropdown-layout-2-left-container > a:nth-child(16)")
    nav_bar_platform_ai = (By.CSS_SELECTOR, "#navbarNavDropdown > ul:nth-child(1) > li.nav-item.dropdown.show > div > div.new-menu-dropdown-layout-2-left-container > a:nth-child(17)")
    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(test_Data.url)

    def accept_cookies(self):
        try:
            self.click_element(self.accept_cookies_button)
        except:
            pass

    def home_page_nav_bar_why_insider(self):
        self.click_navigation_bar_elements(self.why_insider_link, self.why_insider_insider_difference)

    def home_page_nav_bar_compare_vendors(self):
        self.click_navigation_bar_elements(self.why_insider_link, self.why_insider_compare_vendors)

    def home_page_nav_bar_switch_to_insider(self):
        self.click_navigation_bar_elements(self.why_insider_link, self.why_insider_switch_to_insider)

    def home_page_nav_bar_platform(self):
        self.click_navigation_bar_elements(self.nav_bar_platform, self.nav_Bar_platform_overview)

    def home_page_nav_bar_platform_customer_data_management(self):
        self.click_navigation_bar_elements(self.nav_bar_platform, self.nav_bar_platform_customer_data_management)
        #self.driver.back()

    def home_page_nav_bar_platform_customer_profiles(self):
        self.click_navigation_bar_elements(self.nav_bar_platform, self.nav_bar_platform_customer_profiles)

    def home_page_nav_bar_platform_predict_behavior(self):
        self.click_navigation_bar_elements(self.nav_bar_platform, self.nav_bar_platform_predict_behavior)

    def home_page_nav_bar_platform_personalization(self):
        self.click_navigation_bar_elements(self.nav_bar_platform, self.nav_bar_platform_personalization)

    def home_page_nav_bar_platform_recommendations(self):
        self.click_navigation_bar_elements(self.nav_bar_platform, self.nav_bar_platform_recommendations)

    def home_page_nav_bar_platform_cdm_audience_segmengtation(self):
        self.click_navigation_bar_elements(self.nav_bar_platform, self.nav_bar_platform_cdm_audience_segmengtation)

    def home_page_nav_bar_platform_cdm_integrations(self):
        self.click_navigation_bar_elements(self.nav_bar_platform, self.nav_bar_platform_cdm_integrations)

    def home_page_nav_bar_platform_personalization_vsd(self):
        self.click_navigation_bar_elements(self.nav_bar_platform, self.nav_bar_platform_personalization_vsd)

    def home_page_nav_bar_platform_personalization_pre_built(self):
        self.click_navigation_bar_elements(self.nav_bar_platform, self.nav_Bar_platform_personalization_pre_built)

    def home_page_nav_bar_platform_personalization_site_search(self):
        self.click_navigation_bar_elements(self.nav_bar_platform, self.nav_bar_platform_personalization_site_search)

    def home_page_nav_bar_platform_personalization_ab_Testing(self):
        self.click_navigation_bar_elements(self.nav_bar_platform, self.nav_bar_platform_personalization_ab_Testing)

    def home_page_nav_bar_platform_journey_orchestration(self):
        self.click_navigation_bar_elements(self.nav_bar_platform, self.nav_bar_platform_journey_orchestration)

    def home_page_nav_bar_platform_insight_analytics(self):
        self.click_navigation_bar_elements(self.nav_bar_platform, self.nav_bar_platform_insight_analytics)

    def home_page_nav_bar_platform_behavorial_analytics(self):
        self.click_navigation_bar_elements(self.nav_bar_platform, self.nav_bar_platform_behavorial_analytics)

    def home_page_nav_bar_platform_ai(self):
        self.click_navigation_bar_elements(self.nav_bar_platform, self.nav_bar_platform_ai)
