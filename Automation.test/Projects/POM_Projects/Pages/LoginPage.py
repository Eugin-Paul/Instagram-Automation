class LoginPage:
    def __init__(self, driver):
        self.driver = driver

        self.username_textbox = "/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div[2]/div/label/input"
        self.password_textbox = "/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div[3]/div/label/input"
        self.login_button = "/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div[4]"
        self.not_now = "/html/body/div[1]/section/main/div/div/div/div/button"

    def enter_username(self, username):
        self.driver.find_element_by_xpath(self.username_textbox).clear()
        self.driver.find_element_by_xpath(self.username_textbox).send_keys(username)

    def enter_password(self, password):
        self.driver.find_element_by_xpath(self.password_textbox).clear()
        self.driver.find_element_by_xpath(self.password_textbox).send_keys(password)

    def click_login(self):
        self.driver.find_element_by_xpath(self.login_button).click()

    def click_not_now(self):
        self.driver.find_element_by_xpath(self.not_now).click()
