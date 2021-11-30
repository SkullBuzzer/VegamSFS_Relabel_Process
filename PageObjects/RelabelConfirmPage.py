import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By


class RelabelConfirmPage:
    optionRelabel = (By.XPATH, "//a[@id='ContentPlaceHolder_hypRelabel']/div")
    btnPrintLabel = (By.XPATH, "//div[@class='grid_4']/a")
    txtPartUnit = (By.CSS_SELECTOR, "input[name='PartUnit']")
    gridPalletInfo = (By.XPATH, "//a[@id='lnkPalletInfo']")
    btnContinue = (By.XPATH, "//a[@class='ui-btn ui-mini ui-icon-arrow-r ui-btn-icon-left btn-success']")
    txtFromLabel = (By.XPATH, "//input[@id='txtScanFromLabel']")
    txtToLabel = (By.XPATH, "//input[@id='txtScanToLabel']")
    btnConfirm = (By.XPATH, "//button[@id='hypRelabelConfirmQty']")

    def __init__(self, driver):
        self.driver = driver

    def clickOnRelabelOption(self):
        self.driver.find_element(*self.optionRelabel).click()

    def selectReqIDRelabelConf(self, RelID):
        n = len(self.driver.find_elements_by_xpath("//tbody[@id='tbody_239']/tr"))
        for r in range(1, n + 1):
            Req_no = self.driver.find_element_by_xpath("//tbody[@id='tbody_239']/tr[" + str(r) + "]/td[2]").text
            if Req_no == RelID:
                self.driver.find_element_by_xpath("//tbody[@id='tbody_239']/tr[" + str(r) + "]/td[1]").click()

    def getToMaterial_Batch(self):
        toMaterial = self.driver.find_element_by_xpath("//table[@class='table table-bordered table-striped']/tbody/tr["
                                                       "1]/td[19]").text
        action = ActionChains(self.driver)
        element = self.driver.find_element_by_xpath("//table[@class='table table-bordered table-striped']/tbody/tr["
                                                    "1]/td[22]")
        action.move_to_element(element).perform()
        toBatch = self.driver.find_element_by_xpath("//table[@class='table table-bordered table-striped']/tbody/tr["
                                                    "1]/td[22]").text
        return toMaterial, toBatch

    def getPackSize(self):
        pack_size = self.driver.find_element_by_xpath("//table[@class='table table-bordered table-striped']/tbody/tr["
                                                      "1]/td[13]").text
        return pack_size

    def clickOnPrintLabel(self):
        self.driver.find_element(*self.btnPrintLabel).click()

    def enterQty(self, reqQty, packSize):
        if reqQty <= packSize:
            self.driver.find_element(*self.txtPartUnit).send_keys(str(reqQty))
        elif reqQty > packSize:
            qty = reqQty / packSize
            b = qty - int(qty)
            print(b)
            s = str(b)
            part_qty = s[2:]
            self.driver.find_element(*self.txtPartUnit).send_keys(part_qty)

    def printLabel(self):
        self.driver.find_element_by_xpath("//button[@id='hypRelabelConfirmQty']").click()
        time.sleep(3)

    def confirmMsg(self):
        act_msg = self.driver.find_element_by_xpath("//div[text()='Label printed successfully, please collect.']").text

        if act_msg == "Label printed successfully, please collect.":
            flag = True
        else:
            self.driver.get_screenshot_as_file("C:\\Users\\Dell\\PycharmProjects\\VegamSFS_Relabel_Process"
                                               "\\ScreenShots\\printLabel.png")
            flag = False
        return flag

    def clickOnOk(self):
        self.driver.find_element_by_xpath("//a[text()='OK']").click()
        time.sleep(3)

    def clickOnPalletInfo(self):
        self.driver.find_element(*self.gridPalletInfo).click()

    def clickOnContinue(self):
        self.driver.find_element(*self.btnContinue).click()

    def scanFromLabel(self):
        return self.driver.find_element(*self.txtFromLabel)

    def scanToLabel(self):
        time.sleep(2)
        return self.driver.find_element(*self.txtToLabel)

    def clickOnConfirm(self):
        self.driver.find_element(*self.btnConfirm).click()
        time.sleep(5)

    def verifyRecord(self):
        act_msg = self.driver.find_element_by_xpath("//div[text()='Successfully confirmed quantity for relabel']").text
        if act_msg == "Successfully confirmed quantity for relabel":
            flag = True
        else:
            flag = False
            self.driver.get_screenshot_as_file("C:\\Users\\Dell\\PycharmProjects\\VegamSFS_Relabel_Process"
                                               "\\ScreenShots\\RELConfirm.png")
        return flag

    def selectRelabelCompleted(self):
        self.driver.find_element_by_xpath("//ul[@id='div_4286']/li[6]").click()
