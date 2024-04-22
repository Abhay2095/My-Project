from selenium import webdriver
import pytest
from PageObject.LoginPage import LoginPage
from utilities.ReadProperties import ReadConfig
from utilities.customLogger import LogGen


class Test_LoginPage:

    baseurl = ReadConfig.getbaseurl()     ##"https://www.saucedemo.com/"
    username = ReadConfig.getusername()    ##"standard_user"
    password = ReadConfig.getpassword()    ##"secret_sauce"

    logger = LogGen.loggen()

    def test_HomePage_title(self, setup):
        self.logger.info("******* test home page title start *******")
        self.driver = setup
        self.driver.get(self.baseurl)
        self.lp = LoginPage(self.driver)
        self.lp.setusername(self.username)
        self.lp.setpassword(self.password)
        self.lp.clicklogin()
        self.logger.info("***** Successfully Login ********")

        act_title = self.driver.title
        if act_title == "Swag Labs":
            assert True
        else:
            self.driver.save_screenshot("E:\\My Project\\Screenshot\\page.png")
            assert False



























