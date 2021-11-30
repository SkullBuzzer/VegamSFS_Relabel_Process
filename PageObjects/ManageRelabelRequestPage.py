import time

from selenium.webdriver.common.by import By


class ManageRelabelRequestPage:
    lnkDispatch = (By.XPATH, "//a[@id='lnkDispatch']")
    mdlRelabel = (By.XPATH, "//a[@id='ContentPlaceHolder1_lnkManageRelabelRequest']/div")
    breadcrumb = (By.XPATH, "//span[text()='Manage Relabel Requests']")

    def __init__(self, driver):
        self.driver = driver

    def clickOnDispatchTab(self):
        self.driver.find_element(*self.lnkDispatch).click()

    def clickOnManageRelabel(self):
        self.driver.find_element(*self.mdlRelabel).click()
        time.sleep(3)

    def breadCrumb(self):
        act_name = self.driver.find_element(*self.breadcrumb).text
        flag = False
        if act_name == "Manage Relabel Requests":
            flag = True
        return flag
