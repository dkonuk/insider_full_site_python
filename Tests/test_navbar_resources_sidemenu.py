from Pages.NavBarResourcesSideMenuPage import NavBarResourcesSideMenuPage
from Test_Data.test_Data import test_Data
import time


class TestNavBarResourcesSideMenu:

    def test_nav_bar_resources_sidemenu(self, fixtureSetup):
        driver = fixtureSetup
        nav_bar_resources_sidemenu = NavBarResourcesSideMenuPage(driver)
        nav_bar_resources_sidemenu.accept_cookies()
        nav_bar_resources_sidemenu.nav_bar_resources_case_Studies()
        time.sleep(1)
        nav_bar_resources_sidemenu.nav_bar_resources_blog()
        time.sleep(1)
        nav_bar_resources_sidemenu.nav_bar_resources_webinars()
        time.sleep(1)
        nav_bar_resources_sidemenu.nav_bar_resources_reports()
        time.sleep(1)
        nav_bar_resources_sidemenu.nav_bar_resources_ebooks_guides()
        time.sleep(1)
        nav_bar_resources_sidemenu.nav_bar_resources_glossary()
        time.sleep(1)