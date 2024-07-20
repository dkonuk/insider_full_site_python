from Pages.NavBarSolutionsPage import NavBarSolutionsPage
from Test_Data.test_Data import test_Data
import time

class TestNavBarSolutions:

    def test_nav_bar_solutions(self, fixtureSetup):
        driver = fixtureSetup
        nav_bar_solutions = NavBarSolutionsPage(driver)
        nav_bar_solutions.accept_cookies()
        nav_bar_solutions.nav_bar_solutions()
        time.sleep(1)
        nav_bar_solutions.nav_bar_solutions_increase_customer_engagement()
        time.sleep(1)
        nav_bar_solutions.nav_bar_solutions_reduce_customer_churn()
        time.sleep(1)