from selenium import webdriver
from selenium.webdriver.common.by import By

class LoginPage:

    text_username_id = "user-name"
    text_password_id = "password"
    btn_login_id = "login-button"

    def __init__(self, driver):
        self.driver = driver

    def setusername(self,username):
        self.driver.find_element(By.ID,self.text_username_id).clear()
        self.driver.find_element(By.ID, self.text_username_id).send_keys(username)

    def setpassword(self,password):
        self.driver.find_element(By.ID, self.text_password_id).clear()
        self.driver.find_element(By.ID, self.text_password_id).send_keys(password)

    def clicklogin(self):
        self.driver.find_element(By.ID, self.btn_login_id).click()



























