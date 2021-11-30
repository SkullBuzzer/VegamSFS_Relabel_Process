import time

from selenium.webdriver.common.by import By


class AssignRelabelRequestPage:
    btnAssign = (By.XPATH, "//button[@id='btnAssignOperator']")
    btnSave = (By.XPATH, "//button[@data-bind='visible: !IsSaveInProgress(), disable:!HasEditAccess()']")
    txtReqID = (By.XPATH, "//input[@id='txt_4288']")
    status = (By.XPATH, "//div[@class='pro-plan col-12 p-1 pro-plan toggle-drp multi-drp']")
    txtStatus = (By.XPATH, "//div[@class='pro-plan col-12 p-1 pro-plan toggle-drp multi-drp']/label/span")
    lnkAdmin = (By.XPATH, "//a[@id='lnkAdmin']")
    lnkDefineRoles = (By.XPATH, "//div[@class='container-fluid master-body mr-right']/div/div/div/div[2]/a/div")
    lnkPermission = (By.XPATH, "//a[@id='ContentPlaceHolder1_lnkPermission']")
    lnkDisptch = (By.XPATH, "//li[@id='ContentPlaceHolder1_lnkDispatch']/a")
    lnkRelabel = (By.XPATH, "//li[@category='Relabel Process']/a")

    def __init__(self, driver):
        self.driver = driver

    def selectRandomRequest(self):
        reqID = self.driver.find_element_by_xpath("//table[@class='table table-bordered table-striped']/tbody/tr["
                                                  "1]/td[3]").text
        self.driver.find_element_by_xpath("//table[@class='table table-bordered table-striped']/tbody/tr[1]/td["
                                          "1]/span/input").click()
        return reqID

    def clickOnAssign(self):
        self.driver.find_element(*self.btnAssign).click()
        time.sleep(5)

    def getMaxRows(self):
        return len(self.driver.find_elements_by_xpath("//div[@class='modal-body pb-2']/fieldset/div"))

    def selectRelGroup(self, Name):
        n = self.getMaxRows()
        flag = False
        for r in range(1, n + 1):
            grpname = self.driver.find_element_by_xpath(
                "//div[@class='modal-body pb-2']/fieldset/div[" + str(r) + "]/span").text
            if grpname == Name:
                self.driver.find_element_by_xpath(
                    "//div[@class='modal-body pb-2']/fieldset/div[" + str(r) + "]/i[1]").click()
                flag = True
                break
        return flag

    def clickOnSave(self):
        self.driver.find_element(*self.btnSave).click()

    def clickOnReset(self):
        self.driver.find_element_by_xpath("//a[@class='text-centerfull-width bold reset-btn']").click()
        time.sleep(2)

    def enterReqID(self):
        return self.driver.find_element(*self.txtReqID)

    def selectStatusAssign(self):
        self.driver.find_element_by_xpath("//ul[@id='div_4286']/li[2]").click()

    def verifyStatus(self, relID):
        act_status = self.driver.find_element(*self.txtStatus).text
        act_relID = self.driver.find_element_by_xpath("//table[@class='table table-bordered table-striped']/tbody/tr["
                                                      "1]/td[3]").text
        flag = False
        if (act_status == 'Assigned') and (act_relID == relID):
            flag = True
        return flag

    def clickOnAdminTab(self):
        self.driver.find_element(*self.lnkAdmin).click()
        time.sleep(2)

    def clickOnDefineRoles(self):
        self.driver.find_element(*self.lnkDefineRoles).click()

    def clickOnPermission(self):
        self.driver.find_element(*self.lnkPermission).click()

    def department(self):
        return self.driver.find_element_by_xpath("//select[@id='drpDepartment']")

    def roles(self):
        time.sleep(2)
        return self.driver.find_element_by_xpath("//select[@id='drpRole']")

    def clickOnDispatch(self):
        self.driver.find_element(*self.lnkDisptch).click()

    def clickOnRelabelProcess(self):
        self.driver.find_element(*self.lnkRelabel).click()

    def getMaxRows_Roles(self):
        return len(self.driver.find_elements_by_xpath("//table[@class='table table-bordered nobox-shadow "
                                                      "noborder-radius']/tbody/tr"))

    def selectReqRole(self):
        n = self.getMaxRows_Roles()
        for r in range(1, n + 1):
            role = self.driver.find_element_by_xpath("//table[@class='table table-bordered nobox-shadow "
                                                     "noborder-radius']/tbody/tr[" + str(r) + "]/td[1]").text
            if role == "Assign relabeling only to myself":
                self.driver.find_element_by_xpath("//table[@class='table table-bordered nobox-shadow "
                                                  "noborder-radius']/tbody/tr[" + str(r) + "]/td[2]").click()
                break

    def assignRelReq(self, Name):
        n = self.getMaxRows()
        flag = False
        for r in range(1, n + 1):
            grpname = self.driver.find_element_by_xpath(
                "//div[@class='modal-body pb-2']/fieldset/div[" + str(r) + "]/span").text
            if grpname == Name:
                self.driver.find_element_by_xpath(
                    "//div[@class='modal-body pb-2']/fieldset/div[" + str(r) + "]/i[2]").click()
                n = len(self.driver.find_elements_by_xpath("//div[@class='operator-block-body row m-0 p-0']/div/span"))



