import time

from PageObjects.LoginPage import LoginPage
from Utilities.BaseClass import BaseClass
from Utilities.customLogger import LogGen
from Utilities.readProperties import ReadConfig
from Utilities import XLUtils


class Test_10_DDT_Login(BaseClass):
    baseURl = ReadConfig.getApplicationURL()
    path = "C:\\Users\\Dell\\PycharmProjects\\VegamSFS_Relabel_Process\\TestData\\LoginData.xlsx"
    log = LogGen.getLogger()

    def test_login_ddt(self):
        self.log.info("***************** Test_10_LoginPage ******************")
        self.log.info("********** test login data driven started *************")
        self.driver.get(self.baseURl)
        lp = LoginPage(self.driver)
        self.rows = XLUtils.getRowCount(self.path, "Sheet1")

        list_status = []
        for r in range(2, self.rows+1):
            self.username = XLUtils.readData(self.path, "Sheet1", r, 1)
            self.password = XLUtils.readData(self.path, "Sheet1", r, 2)
            self.exp = XLUtils.readData(self.path, "Sheet1", r, 3)

            lp.setUserName().send_keys(self.username)
            lp.setPassword().send_keys(self.password)
            lp.clickOnLogin()
            time.sleep(5)

            act_title = self.driver.title
            exp_title = "iPAS-CC"

            if act_title == exp_title:
                if self.exp == "Pass":
                    self.log.info("******* test case passed ********")
                    lp.clickOnSignOut()
                    lp.clickOnLoginAgain()
                    list_status.append("Pass")
                elif self.exp == "Fail":
                    self.log.info("******* test case failed ********")
                    lp.clickOnSignOut()
                    lp.clickOnLoginAgain()
                    list_status.append("Fail")
            elif act_title != exp_title:
                if self.exp == "Pass":
                    self.log.info("***** test case is failed ********")
                    list_status.append("Fail")
                elif self.exp == "Fail":
                    self.log.info("***** test case passed **********")
                    list_status.append("Pass")

            if "Fail" not in list_status:
                self.log.info("******** Login DDt test passed *********")
                assert True
            else:
                self.log.info("******** Login DDt test failed *********")



