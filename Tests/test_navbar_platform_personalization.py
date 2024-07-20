from Pages.HomePage import HomePage
from Test_Data import test_Data
import time

class Test_Navbar_Platform_Personalization:

    def test_home_page_nav_bar_platform_personalization(self, fixtureSetup):
        driver = fixtureSetup
        home_page = HomePage(driver)
        home_page.accept_cookies()
        home_page.home_page_nav_bar_platform()
        time.sleep(1)
        home_page.home_page_nav_bar_platform_personalization()
        time.sleep(1)
        home_page.home_page_nav_bar_platform_recommendations()
        time.sleep(1)
        home_page.home_page_nav_bar_platform_personalization_vsd()
        time.sleep(1)
        home_page.home_page_nav_bar_platform_personalization_pre_built()
        time.sleep(1)
        home_page.home_page_nav_bar_platform_personalization_site_search()
        time.sleep(1)
        home_page.home_page_nav_bar_platform_personalization_ab_Testing()