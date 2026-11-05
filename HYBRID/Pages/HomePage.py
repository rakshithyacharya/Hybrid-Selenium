class HomePage:
    myinfo="//span[text()='My Info']"


    def __init__(self, driver):
        self.driver = driver
    def my_info(self):
        self.driver.find_element('xpath', self.myinfo).click()
        