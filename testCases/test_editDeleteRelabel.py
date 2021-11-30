import pytest

from PageObjects.AddRelabelRequestPage import AddRelabelRequestPage
from PageObjects.AssignRelabelRequestPage import AssignRelabelRequestPage
from PageObjects.EditDeleteRelabelPage import EditDeleteRelabelPage
from PageObjects.LoginPage import LoginPage
from PageObjects.ManageRelabelRequestPage import ManageRelabelRequestPage
from TestData.testData_editDelete import TestData_EditDelete
from Utilities.BaseClass import BaseClass
from Utilities.customLogger import LogGen
from Utilities.readProperties import ReadConfig


class Test_004_editDeleteRelabel(BaseClass):
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUsername()
    password = ReadConfig.getPassword()
    log = LogGen.getLogger()

    @pytest.mark.run(order=9)
    def test_editRelabelRequest(self, getData_editDel):
        self.log.info("*************** Test_004_editDeleteRelabel **************")
        self.log.info("*************** test edit Relabel Request ***************")
        self.driver.get(self.baseURL)
        lp = LoginPage(self.driver)
        lp.setUserName().send_keys(self.username)
        lp.setPassword().send_keys(self.password)
        lp.clickOnLogin()
        self.log.info("*************** Login Successful *****************")
        mrp = ManageRelabelRequestPage(self.driver)
        mrp.clickOnDispatchTab()
        mrp.clickOnManageRelabel()
        self.log.info("***** Manage Relabel Request Page accessed successfully *********")
        add_rel = AddRelabelRequestPage(self.driver)
        add_rel.clickOnDefineSearchCriteria()
        assi_rel = AssignRelabelRequestPage(self.driver)
        add_rel.clickOnStatus()
        add_rel.selectStatusRequested()
        add_rel.clickOnSearch()
        edit_rel = EditDeleteRelabelPage(self.driver)
        relID = edit_rel.selectRandomRequest()
        edit_rel.clickOnEditIcon()
        edit_rel.updateToBatch().send_keys(getData_editDel['ToBatch'])
        status = edit_rel.clickOnSave()
        assert status == True
        add_rel.clickOnDefineSearchCriteria()
        assi_rel.enterReqID().send_keys(relID)
        add_rel.clickOnSearch()
        edit_rel.clickOnEditIcon()
        status = edit_rel.verifyNewBatch(getData_editDel['ToBatch'])
        assert status == True
        self.log.info("********* test edit Relabel Request passed *************")
        lp.clickOnSignOut()
        lp.clickOnLoginAgain()

    @pytest.mark.run(order=10)
    def test_deleteRelabelRequest(self, getData_editDel):
        self.log.info("*************** test edit Relabel Request ***************")
        self.driver.get(self.baseURL)
        lp = LoginPage(self.driver)
        lp.setUserName().send_keys(self.username)
        lp.setPassword().send_keys(self.password)
        lp.clickOnLogin()
        self.log.info("*************** Login Successful *****************")
        mrp = ManageRelabelRequestPage(self.driver)
        mrp.clickOnDispatchTab()
        mrp.clickOnManageRelabel()
        add_rel = AddRelabelRequestPage(self.driver)
        add_rel.clickOnDefineSearchCriteria()
        assi_rel = AssignRelabelRequestPage(self.driver)
        add_rel.clickOnStatus()
        add_rel.selectStatusRequested()
        add_rel.clickOnSearch()
        edit_rel = EditDeleteRelabelPage(self.driver)
        relID = edit_rel.selectRandomRequest()
        edit_rel.clickOnDeleteIcon()
        edit_rel.clickOnConfirmButton()
        assi_rel.enterReqID().send_keys(relID)
        add_rel.clickOnSearch()
        status = edit_rel.verifyDeleteRecord()
        assert status == True
        self.log.info("************* test edit Relabel Request passed ****************")
        lp.clickOnSignOut()
        lp.clickOnLoginAgain()

    @pytest.fixture(params=TestData_EditDelete.test_data_edit)
    def getData_editDel(self, request):
        return request.param
