class ContactDetails1:
    street1='//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div/div[1]/div/div[2]/input'
    street2='//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div/div[2]/div/div[2]/input'
    city='//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div/div[3]/div/div[2]/input'

    def __init__(self, driver):
        self.driver = driver

    def Contact_details1(self,st1,st2,ct):
        self.driver.find_element('xpath', self.street1).clear()
        self.driver.find_element('xpath', self.street1).send_keys(st1)
        self.driver.find_element('xpath', self.street2).clear()
        self.driver.find_element('xpath', self.street2).send_keys(st2)
        self.driver.find_element('xpath', self.city).clear()
        self.driver.find_element('xpath', self.city).send_keys(ct)
