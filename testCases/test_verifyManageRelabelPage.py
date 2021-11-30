import pytest

from PageObjects.LoginPage import LoginPage
from PageObjects.ManageRelabelRequestPage import ManageRelabelRequestPage
from Utilities.BaseClass import BaseClass
from Utilities.customLogger import LogGen
from Utilities.readProperties import ReadConfig


class Test_001_VerifyManageRelabelPage(BaseClass):
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUsername()
    password = ReadConfig.getPassword()
    log = LogGen.getLogger()

    @pytest.mark.run(order=1)
    def test_verifyManageRelabel(self):
        self.log.info("************* Test_001_VerifyManageRelabel Page **************")

        self.log.info("************ test verify manage relabel page started **********")
        self.driver.get(self.baseURL)
        lp = LoginPage(self.driver)
        lp.setUserName().send_keys(self.username)
        lp.setPassword().send_keys(self.password)
        lp.clickOnLogin()
        self.log.info("********************* Login Successful ***********************")
        mrp = ManageRelabelRequestPage(self.driver)
        mrp.clickOnDispatchTab()
        mrp.clickOnManageRelabel()
        status = mrp.breadCrumb()
        assert status == True
        self.log.info("****** Manage Relabel Request Page accessed successfully ******")
        lp.clickOnSignOut()
        lp.clickOnLoginAgain()
