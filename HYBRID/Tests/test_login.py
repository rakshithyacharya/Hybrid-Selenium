import time

from Pages.LoginPage import LoginPage
from Pages.HomePage import HomePage
from Pages.ContactDetails import ContactDetails
from Pages.ContactDetails1 import ContactDetails1
from Utilities.excel_reader import read_login_data
# from Utilities.dataentry import read_details

def test_orangehrm_login(setup):
    driver = setup
    L = LoginPage(driver)
    HP=HomePage(driver)
    CD=ContactDetails(driver)
    CD1 = ContactDetails1(driver)
    data_path = r'Test_data\login_data.xlsx'
    login_data = read_login_data(data_path)
    # Contact_data=read_details(data_path)

    for un, pwd,st1,st2,city in login_data:
        L.login(un, pwd)
        time.sleep(2)
        if "dashboard" not in driver.current_url:
            driver.get_screenshot_as_file(r'screenshots\failure.png')
            print("Login Failed")
        else:
            print("Login Passed")
            HP.my_info()
            time.sleep(3)
            CD.Contact_details()
            time.sleep(3)
            CD1.Contact_details1(st1, st2, city)
            time.sleep(5)
            if "contactDetails" not in driver.current_url:
                # driver.get_screenshot_as_file(r'screenshots\failure.png')
                print("Login Failed")
            else:
                print("Login Passed")
            driver.find_element('xpath','//*[@id="app"]/div[1]/div[1]/header/div[1]/div[3]/ul/li/span').click()
            driver.find_element('xpath','//*[@id="app"]/div[1]/div[1]/header/div[1]/div[3]/ul/li/ul/li[4]/a').click()

        time.sleep(2)