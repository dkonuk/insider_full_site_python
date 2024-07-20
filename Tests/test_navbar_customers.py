from Pages.NavBarCustomersPage import NavBarSolutionsPage
from Test_Data.test_Data import test_Data
import time

class TestNavBarCustomers:

    def test_nav_bar_customers(self, fixtureSetup):
        driver = fixtureSetup
        nav_bar_customers = NavBarSolutionsPage(driver)
        nav_bar_customers.accept_cookies()
        nav_bar_customers.nav_bar_customers()