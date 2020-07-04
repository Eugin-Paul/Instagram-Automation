import time


class DetailPage:
    def __init__(self, driver):
        self.driver = driver

        self.home = "/html/body/div[1]/section/nav/div[2]/div/div/div[3]/div/div[1]/div/a/svg"
        self.search = "//html/body/div[1]/section/nav/div[2]/div/div/div[2]/input"
        self.search_button = "/html/body/div[1]/section/nav/div[2]/div/div/div[2]/div[2]/div[2]/div/a[1]/div/div[" \
                             "2]/div/span "
        self.search_button_new = "/html/body/div[1]/section/nav/div[2]/div/div/div[2]/div[2]/div[2]/div/a[1]/div"

    # for returning to home page
    def home_click(self):
        self.driver.find_element_by_xpath(self.home).click()
        time.sleep(4)

    # for clicking on profile and scrolling posts
    def scroll_posts(self, search):
        self.driver.find_element_by_xpath(self.search).send_keys(search)
        time.sleep(2)
        self.driver.find_element_by_xpath(self.search_button).click()
        time.sleep(6)
        self.driver.execute_script("window.scrollTo(0, 100)")
        time.sleep(2)
        self.driver.execute_script("window.scrollTo(0, 600)")
        time.sleep(2)
        self.driver.execute_script("window.scrollTo(0, 1200)")
        time.sleep(2)
        self.driver.execute_script("window.scrollTo(0, 1800)")
        time.sleep(2)

    # for profile view and scroll
    def profile_scroll(self, search):
        self.driver.find_element_by_xpath(self.search).send_keys(search)
        time.sleep(4)
        self.driver.find_element_by_xpath(self.search_button_new).click()
        self.driver.refresh()
        self.driver.execute_script("window.scrollTo(0, 600)")
        time.sleep(2)
        self.driver.execute_script("window.scrollTo(0, -500)")
