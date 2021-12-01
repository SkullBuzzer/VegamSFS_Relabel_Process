import pytest

from PageObjects.AddRelabelRequestPage import AddRelabelRequestPage
from PageObjects.AssignRelabelRequestPage import AssignRelabelRequestPage
from PageObjects.EditDeleteRelabelPage import EditDeleteRelabelPage
from PageObjects.LoginPage import LoginPage
from PageObjects.ManageRelabelRequestPage import ManageRelabelRequestPage
from PageObjects.PrintRelabelPage import PrintRelabelPage
from Utilities.BaseClass import BaseClass
from Utilities.customLogger import LogGen
from Utilities.readProperties import ReadConfig


class Test_005_PrintRelabel(BaseClass):
    baseURl = ReadConfig.getApplicationURL()
    username = ReadConfig.getUsername()
    password = ReadConfig.getPassword()
    log = LogGen.getLogger()

    @pytest.mark.regression
    @pytest.mark.run(order=11)
    def test_prePrintRelabel(self):
        self.log.info("*************** Test_005_PrintRelabel *****************")
        self.log.info("*************** test pre print relabel ****************")
        self.driver.get(self.baseURl)
        lp = LoginPage(self.driver)
        lp.setUserName().send_keys(self.username)
        lp.setPassword().send_keys(self.password)
        lp.clickOnLogin()
        self.log.info("*************** Logged in Successfully *****************")
        mrp = ManageRelabelRequestPage(self.driver)
        mrp.clickOnDispatchTab()
        mrp.clickOnManageRelabel()
        self.log.info("******** Manage relabel request page accessed successfully ********")
        ed_rel = EditDeleteRelabelPage(self.driver)
        relID = ed_rel.selectRandomRequest()
        pr_rel = PrintRelabelPage(self.driver)
        pr_rel.clickOnPrintIcon()
        pr_rel.setPartBagUnit().send_keys('25')
        pr_rel.setNoOfLabels().send_keys('1')
        pr_rel.clickOnPrint()
        status = pr_rel.verifyMsg()
        assert status == True
        self.log.info("************* New label printed successfully ****************")
        pr_rel.clickOnClose()
        add_rel = AddRelabelRequestPage(self.driver)
        add_rel.clickOnDefineSearchCriteria()
        assi_rel = AssignRelabelRequestPage(self.driver)
        assi_rel.enterReqID().send_keys(relID)
        add_rel.clickOnSearch()
        material = pr_rel.toMaterial()
        batch = pr_rel.toBatch()
        pr_rel.clickOnPalletInfoTab()
        pr_rel.clickOnPalletLabelInfo()
        pr_rel.setMaterial().send_keys(material)
        pr_rel.setBatch().send_keys(batch)
        pr_rel.clickOnSearch()
        mat_status, bat_status = pr_rel.verifyPrintedLabel()
        if (mat_status == material) and (bat_status == batch):
            assert True
        else:
            self.driver.get_screenshot_as_file(
                "C:\\Users\\Dell\\PycharmProjects\\VegamSFS_Relabel_Process\\ScreenShots\\Label_FG.png")
            assert False








