from Pages.HomePage import HomePage
from Test_Data import test_Data
import time

class Test_Navbar_Platform_CDM:

    def test_home_page_nav_bar_platform(self, fixtureSetup):
        driver = fixtureSetup
        home_page = HomePage(driver)
        home_page.accept_cookies()
        time.sleep(1)
        home_page.home_page_nav_bar_platform_customer_data_management()
        time.sleep(1)
        home_page.home_page_nav_bar_platform_customer_profiles()
        time.sleep(1)
        home_page.home_page_nav_bar_platform_predict_behavior()
        time.sleep(1)
        home_page.home_page_nav_bar_platform_cdm_audience_segmengtation()
        time.sleep(1)
        home_page.home_page_nav_bar_platform_cdm_integrations()


