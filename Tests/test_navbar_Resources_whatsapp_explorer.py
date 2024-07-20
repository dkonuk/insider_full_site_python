from Pages.NavBarResourcesPage import NavBarResourcesPage
from Test_Data.test_Data import test_Data
import time

class TestNavBarResourcesCdpExplorer:

    def test_nav_bar_resources_take_tour(self, fixtureSetup):
        driver = fixtureSetup
        nav_bar_resources = NavBarResourcesPage(driver)
        nav_bar_resources.accept_cookies()
        nav_bar_resources.click_navbar_whatsapp_explorer()
