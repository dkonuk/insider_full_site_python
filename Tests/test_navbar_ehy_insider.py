from Pages.HomePage import HomePage
from Test_Data import test_Data
import time

class Test_Navbar_Ehy_Insider:

    def test_home_page_nav_bar_why_insider(self, fixtureSetup):
        driver = fixtureSetup
        home_page = HomePage(driver)
        home_page.accept_cookies()
        time.sleep(1)
        home_page.home_page_nav_bar_why_insider()
        time.sleep(1)
        home_page.home_page_nav_bar_compare_vendors()
        time.sleep(1)
        home_page.home_page_nav_bar_switch_to_insider()