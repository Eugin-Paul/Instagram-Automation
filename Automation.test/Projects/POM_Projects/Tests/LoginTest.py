from selenium import webdriver
import unittest
from selenium.webdriver.chrome.options import Options
from Projects.POM_Projects.Pages.LoginPage import LoginPage
from Projects.POM_Projects.Pages.MainPage import MainPage
from Projects.POM_Projects.Pages.DetailPage import DetailPage


class MyTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        option = Options()

        option.add_argument("--disable-infobars")
        option.add_argument("start-maximized")
        option.add_argument("--disable-extensions")
        option.add_experimental_option("prefs", {
            "profile.default_content_setting_values.notifications": 1
        })
        cls.driver = webdriver.Chrome(executable_path = r"C:\Users\Dell\PycharmProjects\Automation.test\drivers"
                                                        r"\chromedriver.exe", options = option)
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()

    def test_01_login_page(self):
        driver = self.driver

        driver.get("https://www.instagram.com/")

        login = LoginPage(driver)
        login.enter_username("emailforautomation17@gmail.com")
        login.enter_password("Automation")
        login.click_login()
        login.click_not_now()

    def test_02_main_page(self):
        driver = self.driver

        main = MainPage(driver)
        main.search_textbox("eugiiinn")
        main.profile_click()
        main.edit_profile("checking")

    def test_03_public_page(self):
        driver = self.driver

        detail = DetailPage(driver)
        driver.back()
        detail.scroll_posts("virat.kohli")
        driver.refresh()
        detail.profile_scroll("eugiiinn")
    @classmethod
    def tearDownClass(cls):

        cls.driver.close()
        cls.driver.quit()


if __name__ == '__main__':
    unittest.main()
