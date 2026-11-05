class ContactDetails:
    CD="//a[text()='Contact Details']"

    def __init__(self, driver):
        self.driver = driver

    def Contact_details(self):
        self.driver.find_element('xpath', self.CD).click()

