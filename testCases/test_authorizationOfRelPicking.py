from PageObjects.LoginPage import LoginPage
from PageObjects.ManageRelabelRequestPage import ManageRelabelRequestPage
from PageObjects.RelabelPickingPage import RelabelPickingPage
from Utilities.BaseClass import BaseClass
from Utilities.customLogger import LogGen
from Utilities.readProperties import ReadConfig


class Test_007_authorizationOfRelPicking(BaseClass):
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUsername()
    password = ReadConfig.getPassword()
    log = LogGen.getLogger()

    def test_authorizationOfRelPicking(self):
        self.driver.implicitly_wait(10)
        self.log.info("********** Test_007_authorizationOfRelPicking ***********")

        self.log.info("******* Test authorization of Rel picking started ********")
        self.driver.get(self.baseURL)
        lp = LoginPage(self.driver)
        lp.setUserName().send_keys(self.username)
        lp.setPassword().send_keys(self.password)
        lp.clickOnLogin()
        self.log.info("***************** Login Successful *****************")
        mrp = ManageRelabelRequestPage(self.driver)
        mrp.clickOnDispatchTab()
        rel_pick = RelabelPickingPage(self.driver)
        rel_pick.clickOnDispatchMobile()
        rel_pick.clickOnRelabelOption()
        status = rel_pick.verifyModuleNames()
        assert status == True
        self.log.info("****** Test authorization of Rel Picking Passed *******")

