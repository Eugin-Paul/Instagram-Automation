import time


class MainPage:

    def __init__(self, driver):
        self.driver = driver

        self.search = "//html/body/div[1]/section/nav/div[2]/div/div/div[2]/input"
        self.search_button = "/html/body/div[1]/section/nav/div[2]/div/div/div[2]/div[2]/div[2]/div/a[1]/div/div[" \
                             "2]/div/span "
        self.profile = "/html/body/div[1]/section/nav/div[2]/div/div/div[3]/div/div[5]/a/img"
        self.home = "/html/body/div[1]/div[2]/div/div[1]/div/div/div/div[2]/div[1]/div[2]/div/a"
        self.edit_profile_name = "/html/body/div[1]/section/main/div/header/section/div[1]/a/button"
        self.bio_text = "pepBio"
        self.submit = "/html/body/div[1]/section/main/div/article/form/div[10]/div/div/button[1]"

    # for scroll feed and searching the name
    def search_textbox(self, search):
        self.driver.execute_script("window.scrollTo(0, 600)")
        time.sleep(2)
        self.driver.execute_script("window.scrollTo(0, 1200)")
        time.sleep(2)
        self.driver.execute_script("window.scrollTo(0, 1800)")
        time.sleep(2)
        self.driver.find_element_by_xpath(self.search).send_keys(search)
        time.sleep(2)
        self.driver.find_element_by_xpath(self.search_button).click()
        time.sleep(6)

    # for clicking the profile
    def profile_click(self):
        self.driver.find_element_by_xpath(self.profile).click()
        time.sleep(6)

    # to edit the profile and changing bio name
    def edit_profile(self, bio_text):
        self.driver.find_element_by_xpath(self.edit_profile_name).click()
        time.sleep(6)
        self.driver.find_element_by_id(self.bio_text).clear()
        self.driver.find_element_by_id(self.bio_text).send_keys(bio_text)
        time.sleep(3)
        self.driver.find_element_by_xpath(self.submit).click()
        time.sleep(6)

