import time
import re

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class RelabelPickingPage:
    lnkDispatch = (By.XPATH, "//a[@id='ContentPlaceHolder1_lnkDispatchMobile']/div")
    lnkRelabel = (By.XPATH, "//a[@id='ContentPlaceHolder_hypRelabel']/div")
    moduleNames = (By.XPATH, "//div[@id='divRelabelMainContent']/div/a/div/div[2]/h4")
    lnkPick = (By.XPATH, "//a[@id='ContentPlaceHolder_hypPick']/div")
    btnContinue = (By.XPATH, "//a[@class='ui-btn ui-mini ui-icon-arrow-r ui-btn-icon-left btn-success']")
    txtScanBin = (By.XPATH, "//input[@id='txtScanBinValue']")
    btnPick = (By.XPATH, "//a[@id='btnPick']")
    lnkPalletInfoTab = (By.XPATH, "//a[@id='lnkPalletInfo']")
    btnSearch = (By.XPATH, "//button[@id='ContentPlaceHolder1_btnSearch']/i")
    lnkPalletInfo = (By.XPATH, "//a[@id='ContentPlaceHolder1_lnkPalletInfo']/div")
    txtMaterialPalletInfo = (By.XPATH, "//input[@id='txtMatNumber']")
    txtBatchPalletInfo = (By.XPATH, "//input[@id='txtBatchNumber']")
    txtLabel = (By.XPATH, "//input[@id='txtScanLabel']")
    textEnterQty = (By.XPATH, "//input[@id='txtPickedQty']")
    btnConfirm = (By.XPATH, "//button[@id='hypRelabelConfirmQty']")
    homeIcon = (By.XPATH, "//a[@id='hypheaderHomeIcon']")
    lnkPickingCompl = (By.XPATH, "//ul[@id='div_4286']/li[4]")
    lnkGrid = (By.XPATH, "//a[@id='hdrToggle']")
    gridDispatch = (By.XPATH, "//a[@id='lnkDispatch']")

    def __init__(self, driver):
        self.driver = driver

    def clickOnDispatchMobile(self):
        self.driver.find_element(*self.lnkDispatch).click()

    def clickOnRelabelOption(self):
        self.driver.find_element(*self.lnkRelabel).click()

    def verifyModuleNames(self):
        l1 = ["Pick", "Re-Label", "Re-Print Label", "Bin To Bin"]
        l2 = []
        names = self.driver.find_elements(*self.moduleNames)
        for name in names:
            act_name = name.text
            l2.append(act_name)
        if l1 == l2:
            flag = True
        else:
            self.driver.get_screenshot_as_file("C:\\Users\\Dell\\PycharmProjects\\VegamSFS_Relabel_Process"
                                               "\\ScreenShots\\RelPick.png")
            flag = False
        return flag

    def clickOnPickOption(self):
        self.driver.find_element(*self.lnkPick).click()
        wait = WebDriverWait(self.driver, 10)
        wait.until(
            EC.presence_of_element_located((By.XPATH, "//a[@class='ui-btn ui-mini ui-icon-arrow-r ui-btn-icon-left "
                                                      "btn-success']")))

    def getMaterial_batch(self):
        material = self.driver.find_element_by_xpath("//table[@class='table table-bordered table-striped']/tbody/tr["
                                                     "1]/td[6]").text
        batch = self.driver.find_element_by_xpath("//table[@class='table table-bordered table-striped']/tbody/tr["
                                                  "1]/td[9]").text
        return material, batch

    def getRequestedQty(self):
        ReqQty = self.driver.find_element_by_xpath("//table[@class='table table-bordered table-striped']/tbody/tr["
                                                   "1]/td[11]").text
        return ReqQty

    def clickOnPalletInfoTab(self):
        self.driver.find_element(*self.lnkPalletInfoTab).click()

    def clickOnPalletInfoModule(self):
        self.driver.find_element(*self.lnkPalletInfo).click()
        time.sleep(3)

    def setMaterialCode(self):
        return self.driver.find_element(*self.txtMaterialPalletInfo)

    def setBatch(self):
        return self.driver.find_element(*self.txtBatchPalletInfo)

    def clickOnSearch(self):
        self.driver.find_element(*self.btnSearch).click()
        time.sleep(3)

    def getRmLabel(self):
        return self.driver.find_element_by_xpath("//table[@id='tablePalletInfo']/tbody/tr[1]/td[2]").text

    def selectReqIDForPick(self, relID):
        n = len(self.driver.find_elements_by_xpath("//table[@class='ui-table ui-body-d ui-shadow ui-responsive "
                                                   "media-table']/tbody/tr"))
        for r in range(1, n + 1):
            act_req = self.driver.find_element_by_xpath("//table[@class='ui-table ui-body-d ui-shadow ui-responsive "
                                                        "media-table']/tbody/tr[" + str(r) + "]/td[2]").text
            if act_req == relID:
                self.driver.find_element_by_xpath("//table[@class='ui-table ui-body-d ui-shadow ui-responsive "
                                                  "media-table']/tbody/tr[" + str(r) + "]/td[1]").click()
                break

    def clickOnContinue(self):
        time.sleep(3)
        self.driver.find_element(*self.btnContinue).click()

    def scanBinLocation(self):
        s = ""
        bin_name = self.driver.find_element_by_xpath("//tbody[@id='tbdyAvlBin']/tr[1]/td[3]").text
        qty = self.driver.find_element_by_xpath(
            "//table[@id='tableAvailableBins']/tbody/tr[1]/td[5]").text
        l = re.findall('\d*\.?\d+', qty)
        s = float(l[0])

        '''for x in qty:
            if x.isdigit:
                s = s + x
            else:
                pass'''
        self.driver.find_element(*self.txtScanBin).send_keys(bin_name)
        return s, bin_name

    def clickOnPick(self):
        self.driver.find_element(*self.btnPick).click()
        time.sleep(2)

    def scanRmLabel(self):
        return self.driver.find_element(*self.txtLabel)

    def getQty(self, reqQty, bin_qty):

        if reqQty <= bin_qty:
            qty = reqQty
        else:
            qty = bin_qty
        return qty

    def enterQty(self):
        time.sleep(3)
        return self.driver.find_element(*self.textEnterQty)

    def clickOnConfirm(self, req_qty, enter_qty, avail_qty):
        time.sleep(3)
        flag = True
        if enter_qty < int(req_qty):
            self.driver.find_element(*self.btnConfirm).click()
            time.sleep(8)
            if enter_qty == avail_qty:
                self.driver.find_element_by_xpath("//a[@class='ZebraDialog_Button_0']").click()
            time.sleep(7)
            flag = False
        else:
            self.driver.find_element(*self.btnConfirm).click()
            time.sleep(10)

        return flag

    def returnPallet(self):
        return self.driver.find_element_by_xpath("//input[@id='txtTargetBin']")

    def clickOnConfirmBtn(self):
        self.driver.find_element_by_xpath("//a[@id='confirmButton']").click()
        act_msg = self.driver.find_element_by_xpath("//div[text()='Movement is successful']").text
        self.driver.find_element_by_xpath("//a[@class='ZebraDialog_Button_0']").click()
        flag = False
        if act_msg == "Movement is successful":
            flag = True
        else:
            self.driver.get_screenshot_as_file("C:\\Users\\Dell\\PycharmProjects\\VegamSFS_Relabel_Process"
                                               "\\ScreenShots\\RTW.png")
        return flag

    def clickOnHomeIcon(self):
        self.driver.find_element(*self.homeIcon).click()
        time.sleep(3)

    def clickOnGrid(self):
        self.driver.find_element(*self.lnkGrid).click()

    def clickOnDispatch(self):
        self.driver.find_element(*self.gridDispatch).click()
        time.sleep(2)

    def selStatusPickingCompleted(self):
        self.driver.find_element(*self.lnkPickingCompl).click()
