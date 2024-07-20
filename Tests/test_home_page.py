from Pages.HomePage import HomePage
from Test_Data import test_Data
import time

class Test_HomePage:

    def test_home_page_nav_bar(self, fixtureSetup):
        driver = fixtureSetup
        home_page = HomePage(driver)
        home_page.accept_cookies()
        #home_page.home_page_nav_bar_why_insider()
        time.sleep(1)
        #home_page.home_page_nav_bar_compare_vendors()
        time.sleep(1)
        #home_page.home_page_nav_bar_switch_to_insider()
        time.sleep(1)
        #home_page.home_page_nav_bar_platform()
        time.sleep(1)
        #home_page.home_page_nav_bar_platform_customer_data_management()
        time.sleep(1)
        #home_page.home_page_nav_bar_platform_customer_profiles()
        time.sleep(1)
        #home_page.home_page_nav_bar_platform_predict_behavior()
        time.sleep(1)
        home_page.home_page_nav_bar_platform_personalization()
