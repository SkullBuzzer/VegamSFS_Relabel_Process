import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By


class AddRelabelRequestPage:
    btnAddRelabel = (By.XPATH, "//button[@id='ContentPlaceHolder1_btnAddRelabelRequest']")
    selFromRel = (By.XPATH, "//span[@id='select2-drpFromCustomers-container']")
    txtFromKeyCustName = (By.XPATH, "//input[@class='select2-search__field']")
    selFromKeyCustName = (By.XPATH, "//ul[@id='select2-drpFromCustomers-results']/li")
    selFromCustCode = (By.XPATH, "//span[@id='select2-drpFromCustomerCodes-container']")
    txtCustCode = (By.XPATH, "//input[@class='select2-search__field']")
    selFromCustName = (By.XPATH, "//ul[@id='select2-drpFromCustomerCodes-results']/li")
    txtFromMaterial = (By.XPATH, "//input[@id='txtFromMaterial']")
    selFromMaterial = (By.XPATH, "//ul[@id='ui-id-1']/li/div")
    txtFromBatch = (By.XPATH, "//input[@data-bind='value:FromBatchNum']")
    txtStorageLoc = (By.XPATH, "//input[@data-bind='value:StorageLocation']")
    txtQty = (By.XPATH, "//input[@data-bind='value:Quantity']")
    dropDown = (By.XPATH, "//select[@class='form-control h-30 w-100 custom-select']")
    txtRemarks = (By.XPATH, "//textarea[@data-bind='value:Remarks']")

    selToRelabel = (By.XPATH, "//span[@id='select2-drpToCustomers-container']")
    txtToKeyCustName = (By.XPATH, "//input[@class='select2-search__field']")
    selTokeyCustName = (By.XPATH, "//ul[@id='select2-drpToCustomers-results']")
    selToCustCode = (By.XPATH, "//span[@id='select2-drpToCustomerCodes-container']")
    txtToCustCode = (By.XPATH, "//input[@class='select2-search__field']")
    selToCustName = (By.XPATH, "//ul[@id='select2-drpToCustomerCodes-results']/li")
    txtToMaterialCode = (By.XPATH, "//input[@id='txtToMaterial']")
    selToMaterialCode = (By.XPATH, "//ul[@id='ui-id-2']/li/div")
    txtToBatch = (By.XPATH, "//input[@data-bind='value:ToBatchNum']")
    manfDate = (By.XPATH, "//input[@id='txtManfDate']")
    expCalendar = (By.XPATH, "//input[@id='txtExpDate']")
    selMonth = (By.XPATH, "//select[@class='ui-datepicker-month']")
    selYear = (By.XPATH, "//select[@class='ui-datepicker-year']")
    reqDateCalen = (By.XPATH, "//input[@id='txtRequestCompletionDate']")
    enlNewCOA = (By.XPATH, "//fieldset[@class='mb-1 px-2 col-12 col-md-6']/label/label/span")
    btnSave = (By.XPATH, "//button[@id='btnSaveRelabelRequest']")
    lnkDefineSearch = (By.XPATH, "//div[@id='divDefineSearchCriteria']")
    status = (By.XPATH, "//label[@class='cursor-pointer multi-drp-lbl']")
    btnSearch = (By.XPATH, "//button[@class='btn btn-primary']")
    txtFromMatnr = (By.XPATH, "//input[@id='txt_4291']")
    txtToBatchNum = (By.XPATH, "//input[@id='txt_4307']")

    def __init__(self, driver):
        self.driver = driver

    def clickOnAddRelabel(self):
        self.driver.find_element(*self.btnAddRelabel).click()
        time.sleep(3)

    def selectRelabelFrom(self):
        self.driver.find_element(*self.selFromRel).click()
        return self.driver.find_element(*self.txtFromKeyCustName)

    def selectFromKeyCustName(self):
        self.driver.find_element(*self.selFromKeyCustName).click()

    def selectFromCustCode(self):
        self.driver.find_element(*self.selFromCustCode).click()

    def setFromCustCode(self):
        return self.driver.find_element(*self.txtCustCode)

    def selectFromCustName(self):
        self.driver.find_element(*self.selFromCustName).click()

    def setFromMaterialCode(self):
        self.driver.find_element(*self.txtFromMaterial).clear()
        return self.driver.find_element(*self.txtFromMaterial)

    def selectFromMaterial(self):
        time.sleep(3)
        self.driver.find_element(*self.selFromMaterial).click()

    def setFromBatch(self):
        return self.driver.find_element(*self.txtFromBatch)

    def setStorageLoc(self):
        return self.driver.find_element(*self.txtStorageLoc)

    def setQuantity(self):
        return self.driver.find_element(*self.txtQty)

    def drop_down(self):
        return self.driver.find_element(*self.dropDown)

    def setRemarks(self):
        return self.driver.find_element(*self.txtRemarks)

    def selectToRelabel(self):
        self.driver.find_element(*self.selToRelabel).click()
        return self.driver.find_element(*self.txtToKeyCustName)

    def selectToKeyCustName(self):
        self.driver.find_element(*self.selTokeyCustName).click()

    def selectToCustCode(self):
        self.driver.find_element(*self.selToCustCode).click()
        return self.driver.find_element(*self.txtToCustCode)

    def selectToCustName(self):
        self.driver.find_element(*self.selToCustName).click()

    def setToMaterialCode(self):
        self.driver.find_element(*self.txtToMaterialCode).clear()
        return self.driver.find_element(*self.txtToMaterialCode)

    def selectToMaterialCode(self):
        time.sleep(3)
        self.driver.find_element(*self.selToMaterialCode).click()

    def setToBatch(self):
        self.driver.find_element(*self.txtToBatch).clear()
        return self.driver.find_element(*self.txtToBatch)

    def setManufactureDate(self, CurrentDate):
        self.driver.find_element(*self.manfDate).click()
        time.sleep(2)
        dates = self.driver.find_elements_by_xpath("//table[@class='ui-datepicker-calendar']//a")
        for date in dates:
            data = date.text
            if data == CurrentDate:
                date.click()
                break

    def clickOnExpCalendar(self):
        self.driver.find_element(*self.expCalendar).click()
        time.sleep(2)

    def setExpiryMonth(self):
        return self.driver.find_element(*self.selMonth)

    def setExpiryYear(self):
        return self.driver.find_element(*self.selYear)

    def setExpiryDate(self, expDate):
        dates = self.driver.find_elements_by_xpath("//table[@class='ui-datepicker-calendar']//a")
        for date in dates:
            data = date.text
            if data == expDate:
                date.click()
                break

    def setRequestDate(self, CurrentDate):
        self.driver.find_element(*self.reqDateCalen).click()
        time.sleep(2)
        dates = self.driver.find_elements_by_xpath("//table[@class='ui-datepicker-calendar']//a")
        for date in dates:
            data = date.text
            if data == CurrentDate:
                date.click()
                break

    def enableNewCOA(self):
        self.driver.find_element(*self.enlNewCOA).click()

    def clickOnSave(self):
        self.driver.find_element(*self.btnSave).click()
        time.sleep(2)
        confirm_msg = self.driver.find_element_by_xpath("//p[@id='alertMessage']").text
        flag = False
        if confirm_msg == "Relabel request saved successfully":
            flag = True
        self.driver.find_element_by_xpath("//button[text()='OK']").click()
        self.driver.find_element_by_xpath("//span[@class='float-right mr-1 cursor-pointer']").click()
        return flag

    def clickOnDefineSearchCriteria(self):
        self.driver.find_element(*self.lnkDefineSearch).click()
        time.sleep(2)

    def clickOnStatus(self):
        self.driver.find_element(*self.status).click()
        time.sleep(2)

    def selectStatusRequested(self):
        self.driver.find_element_by_xpath("//ul[@id='div_4286']/li[1]").click()
        self.driver.find_element_by_xpath("//i[@class='float-right i-chevron-up']").click()

    def enterFromMaterialCode(self):
        return self.driver.find_element(*self.txtFromMatnr)

    def enterToBatchNum(self):
        return self.driver.find_element(*self.txtToBatchNum)

    def clickOnFromReqCalendar(self):
        self.driver.find_element_by_xpath("//input[@id='txtstartvaluectl_4301']").click()
        time.sleep(2)

    def setReqFromMonth(self):
        return self.driver.find_element_by_xpath("//select[@class='ui-datepicker-month']")

    def enterRequestDate(self, currentDate):
        time.sleep(2)
        fromDates = self.driver.find_elements_by_xpath("//table[@class='ui-datepicker-calendar']//a")
        for date in fromDates:
            text = date.text
            if text == currentDate:
                date.click()
                break
        self.driver.find_element_by_xpath("//input[@id='txtendvaluectl_4301']").click()
        time.sleep(2)
        dates = self.driver.find_elements_by_xpath("//table[@class='ui-datepicker-calendar']//a")
        for date in dates:
            text = date.text
            if text == currentDate:
                date.click()
                break

    def clickOnSearch(self):
        self.driver.find_element(*self.btnSearch).click()
        time.sleep(2)

    def verifyStatus(self):
        action = ActionChains(self.driver)
        try:
            action.move_to_element(self.driver.find_element_by_xpath("//div[@class='status grey']")).perform()
            flag = True
        except:
            flag = False
            print("Status not captured")

        return flag

    def clickOnCopyIcon(self):
        self.driver.find_element_by_xpath(
            "//table[@class='table table-bordered table-striped']/tbody/tr/td/span/i[4]").click()

    def expWaitLocator(self):
        return self.driver.find_element_by_xpath("//label[text()='Add Re-label Material Information']").text
