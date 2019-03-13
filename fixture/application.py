from selenium.webdriver.chrome.webdriver import WebDriver
import time


class Application:
    def __init__(self):
        self.wd = WebDriver()
        self.wd.implicitly_wait(3)

    def open_home_page(self):
        wd = self.wd
        wd.get("https://antycaptcha.amberteam.pl:5443/")

    def enter_exercise(self, number):
        wd = self.wd
        string = "EXERCISE %s" %number
        exercises = wd.find_elements_by_xpath("//a[@class='button u-full-width ']")
        for exercise in exercises:
            if string in exercise.text:
                exercise.click()

    def get_page_title(self):
        wd = self.wd
        page_title = wd.find_element_by_xpath("//h1[@class='title']")
        return page_title

    def check_what_buttons_to_push(self):
        pass

    def destroy(self):
        self.wd.quit()