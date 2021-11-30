import time

from selenium.webdriver.common.by import By


class LoginPage:
    txtUsername = (By.XPATH, "//input[@id='ContentPlaceHolder_userNameTextBox']")
    txtPassword = (By.XPATH, "//input[@id='ContentPlaceHolder_passwordTextbox']")
    btnLogin = (By.XPATH, "//input[@id='ContentPlaceHolder_loginButton']")
    lnkLoginAgain = (By.XPATH, "//a[@id='ContentPlaceHolder_lnkLoginAgain']")
    lnkUserProfile = (By.XPATH, "//a[@id='userPropfile']")
    btnSignOut = (By.XPATH, "//a[@id='signOut']")
    lnkDispatch = (By.XPATH, "//a[@id='lnkDispatch']")

    def __init__(self, driver):
        self.driver = driver

    def setUserName(self):
        return self.driver.find_element(*self.txtUsername)

    def setPassword(self):
        return self.driver.find_element(*self.txtPassword)

    def clickOnLogin(self):
        self.driver.find_element(*self.btnLogin).click()
        time.sleep(3)

    def clickOnSignOut(self):
        self.driver.find_element(*self.lnkUserProfile).click()
        time.sleep(1)
        self.driver.find_element(*self.btnSignOut).click()

    def clickOnLoginAgain(self):
        self.driver.find_element(*self.lnkLoginAgain).click()
