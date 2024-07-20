from Pages.HomePage import HomePage
from Test_Data import test_Data
import time

class Test_Navbar_Platform_Restofit:

    def test_home_page_nav_bar_platform_restofit(self, fixtureSetup):
        driver = fixtureSetup
        home_page = HomePage(driver)
        home_page.accept_cookies()
        home_page.home_page_nav_bar_platform()
        time.sleep(1)
        home_page.home_page_nav_bar_platform_journey_orchestration()
        time.sleep(1)
        home_page.home_page_nav_bar_platform_insight_analytics()
        time.sleep(1)
        home_page.home_page_nav_bar_platform_behavorial_analytics()
        time.sleep(1)
        home_page.home_page_nav_bar_platform_ai()

