import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By


class PrintRelabelPage:
    txtPartUnit = (By.XPATH, "//input[@id='txtPartBagUnit']")
    txtNoOfLabels = (By.XPATH, "//input[@id='txtNoOfLabels']")
    btnPrint = (By.XPATH, "//button[@id='btnPrintLabel']")
    lnkPalletInfo = (By.XPATH, "//a[@id='lnkPalletInfo']")
    modulePalletInfo = (By.XPATH, "//a[@id='ContentPlaceHolder1_lnkPalletInfo']/div")
    txtMaterial = (By.XPATH, "//input[@id='txtMatNumber']")
    txtBatch = (By.XPATH, "//input[@id='txtBatchNumber']")
    btnSearch = (By.XPATH, "//button[@id='ContentPlaceHolder1_btnSearch']")

    def __init__(self, driver):
        self.driver = driver

    def clickOnPrintIcon(self):
        self.driver.find_element_by_xpath(
            "//table[@class='table table-bordered table-striped']/tbody/tr/td/span/i[3]").click()

    def setPartBagUnit(self):
        return self.driver.find_element(*self.txtPartUnit)

    def setNoOfLabels(self):
        return self.driver.find_element(*self.txtNoOfLabels)

    def clickOnPrint(self):
        self.driver.find_element(*self.btnPrint).click()

    def verifyMsg(self):
        time.sleep(3)
        act_msg = self.driver.find_element_by_xpath("//span[@id='spnPrinterSettingError']").text
        flag = False
        if act_msg == "Successfully printed Label.":
            flag = True
        else:
            self.driver.get_screenshot_as_file(
                "C:\\Users\\Dell\\PycharmProjects\\VegamSFS_Relabel_Process\\ScreenShots\\print.png")
        return flag

    def toMaterial(self):
        material = self.driver.find_element_by_xpath("//table[@class='table table-bordered "
                                                     "table-striped']/tbody/tr/td[19]").text
        return material

    def toBatch(self):
        action = ActionChains(self.driver)
        element = self.driver.find_element_by_xpath("//table[@class='table table-bordered "
                                                    "table-striped']/tbody/tr/td[22]")
        action.move_to_element(element).perform()
        batch = self.driver.find_element_by_xpath("//table[@class='table table-bordered "
                                                  "table-striped']/tbody/tr/td[22]").text
        return batch

    def clickOnClose(self):
        self.driver.find_element_by_xpath("//div[@id='divPrintRelabelModal']/div/div/div/button").click()

    def clickOnPalletInfoTab(self):
        self.driver.find_element(*self.lnkPalletInfo).click()
        time.sleep(2)

    def clickOnPalletLabelInfo(self):
        self.driver.find_element(*self.modulePalletInfo).click()
        time.sleep(2)

    def setMaterial(self):
        return self.driver.find_element(*self.txtMaterial)

    def setBatch(self):
        return self.driver.find_element(*self.txtBatch)

    def clickOnSearch(self):
        self.driver.find_element(*self.btnSearch).click()
        time.sleep(2)

    def verifyPrintedLabel(self):
        s = self.driver.find_element_by_xpath("//table[@id='tablePalletInfo']/tbody/tr[1]/td[3]").text
        l = s.split('/')
        pr_material = l[0]
        pr_batch = self.driver.find_element_by_xpath("//table[@id='tablePalletInfo']/tbody/tr[1]/td[5]").text
        return pr_material, pr_batch
