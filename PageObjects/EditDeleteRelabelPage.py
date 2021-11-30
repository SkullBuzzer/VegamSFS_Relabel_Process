import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By


class EditDeleteRelabelPage:
    txtToBatch = (By.XPATH, "//input[@data-bind='value:ToBatchNum']")
    btnSave = (By.XPATH, "//button[@id='btnSaveRelabelRequest']")
    btnConfirm = (By.XPATH, "//button[text()='Confirm']")

    def __init__(self, driver):
        self.driver = driver

    def selectRandomRequest(self):
        reqID = self.driver.find_element_by_xpath("//table[@class='table table-bordered table-striped']/tbody/tr["
                                                  "1]/td[3]").text
        return reqID

    def clickOnEditIcon(self):
        self.driver.find_element_by_xpath(
            "//table[@class='table table-bordered table-striped']/tbody/tr/td/span/i[1]").click()

    def updateToBatch(self):
        time.sleep(2)
        self.driver.find_element(*self.txtToBatch).clear()
        return self.driver.find_element(*self.txtToBatch)

    def clickOnSave(self):
        self.driver.find_element(*self.btnSave).click()
        time.sleep(2)
        act_msg = self.driver.find_element_by_xpath("//p[@id='alertMessage']").text
        flag = False
        if act_msg == "Relabel request updated successfully":
            flag = True
        self.driver.find_element_by_xpath("//button[text()='OK']").click()
        self.driver.find_element_by_xpath("//span[@class='float-right mr-1 cursor-pointer']").click()
        return flag

    def verifyNewBatch(self, batch):
        action = ActionChains(self.driver)
        toBatch = self.driver.find_element_by_xpath("//table[@class='table table-bordered "
                                                    "table-striped']/tbody/tr/td[22]/span")
        action.move_to_element(toBatch).perform()
        act_batch = toBatch.text
        flag = False
        if act_batch == batch:
            flag = True
        return flag

    def clickOnDeleteIcon(self):
        self.driver.find_element_by_xpath(
            "//table[@class='table table-bordered table-striped']/tbody/tr/td/span/i[2]").click()

    def clickOnConfirmButton(self):
        self.driver.find_element(*self.btnConfirm).click()

    def verifyDeleteRecord(self):
        flag = False
        act_msg = self.driver.find_element_by_xpath("//span[text()='No records found']").text
        if act_msg == "No records found":
            flag = True
        return flag



