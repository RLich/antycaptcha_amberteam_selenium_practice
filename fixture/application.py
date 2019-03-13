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
        string = "EXERCISE %s" % str(number)
        exercises = wd.find_elements_by_xpath("//a[@class='button u-full-width ']")
        for exercise in exercises:
            if string in exercise.text:
                exercise.click()
                break

    def get_page_title(self):
        wd = self.wd
        page_title = wd.find_element_by_xpath("//h1[@class='title']")
        return page_title.text

    def push_buttons_in_proper_order(self):
        wd = self.wd
        get_buttons = wd.find_elements_by_xpath("//tbody//code")
        button_1 = get_buttons[0]
        button_2 = get_buttons[1]
        button_3 = get_buttons[2]
        print(button_1.text, button_2.text, button_3.text)

        button_1.click()
        button_2.click()
        button_3.click()

    def get_solution_ex_1(self):
        wd = self.wd
        wd.find_element_by_id("solution").click()
        solution = wd.find_element_by_xpath("//div//code[@class='wrap']")
        return solution.text



    def destroy(self):
        self.wd.quit()