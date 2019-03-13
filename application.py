from selenium.webdriver.chrome.webdriver import WebDriver


class Application:
    def __init__(self):
        self.wd = WebDriver()
        self.wd.implicitly_wait(3)

    def open_home_page(self):
        wd = self.wd
        wd.get("https://antycaptcha.amberteam.pl:5443/")

    def enter_first_exercise(self):
        wd = self.wd
        exercises = wd.find_elements_by_xpath("//a[@class='button u-full-width ']")
        for exercise in exercises:
            if exercise.text == 'Exercise 1 - Three buttons':
                exercise.click()

    def destroy(self):
        self.wd.quit()