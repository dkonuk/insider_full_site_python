from Pages.NavBarResourcesPage import NavBarResourcesPage
from Test_Data.test_Data import test_Data
import time

class TestNavBarResources:

    def test_nav_bar_resources(self, fixtureSetup):
        driver = fixtureSetup
        nav_bar_resources = NavBarResourcesPage(driver)
        nav_bar_resources.accept_cookies()
        nav_bar_resources.click_nav_bar_resources_explore_insider()
