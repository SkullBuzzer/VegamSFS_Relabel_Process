import pytest

from PageObjects.AddRelabelRequestPage import AddRelabelRequestPage
from PageObjects.AssignRelabelRequestPage import AssignRelabelRequestPage
from PageObjects.LoginPage import LoginPage
from PageObjects.ManageRelabelRequestPage import ManageRelabelRequestPage
from TestData.testData_AssignRelabelRequest import TestData_AssignRelabel
from Utilities.BaseClass import BaseClass
from Utilities.customLogger import LogGen
from Utilities.readProperties import ReadConfig


class Test_003_assignRelabelRequest(BaseClass):
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUsername()
    password = ReadConfig.getPassword()
    log = LogGen.getLogger()

    @pytest.mark.run(order=5)
    def test_assignRelabelRequestToOperatorGroup(self, getData_assign):
        self.log.info("************* Test_003_assignRelabelRequest ****************")
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
        add_rel.clickOnStatus()
        add_rel.selectStatusRequested()
        add_rel.clickOnSearch()
        assi_rel = AssignRelabelRequestPage(self.driver)
        relID = assi_rel.selectRandomRequest()

        assi_rel.clickOnAssign()
        status = assi_rel.selectRelGroup(getData_assign['RelabelGroup'])
        assert status == True
        assi_rel.clickOnSave()
        self.log.info("*************** Relabel Request Assigned Successfully **************")

        assi_rel.clickOnReset()
        assi_rel.enterReqID().send_keys(relID)
        add_rel.clickOnStatus()
        assi_rel.selectStatusAssign()
        add_rel.clickOnSearch()
        status = assi_rel.verifyStatus(relID)
        assert status == True
        self.log.info("************* Relabel Request status changed to Assigned ***********")

        self.log.info("************** test assign Relabel Request is passed ***************")
        lp.clickOnSignOut()
        lp.clickOnLoginAgain()

    @pytest.mark.skip
    def test_assignRelabelRequestToMyself(self, getData_assign):
        self.driver.implicitly_wait(10)
        self.log.info("*********** test assign Rel Request to my self started ************")
        lp = LoginPage(self.driver)
        lp.setUserName().send_keys(getData_assign['Username'])
        lp.setPassword().send_keys(getData_assign['Password'])
        lp.clickOnLogin()
        self.log.info("*************** Login Successful *****************")
        assi_rel = AssignRelabelRequestPage(self.driver)
        assi_rel.clickOnAdminTab()
        assi_rel.clickOnDefineRoles()
        assi_rel.clickOnPermission()
        self.select_drop_down(assi_rel.department(), 'PLANT MANAGEMENT')
        self.select_drop_down(assi_rel.roles(), 'Plant Admin')
        assi_rel.clickOnDispatch()
        assi_rel.clickOnRelabelProcess()
        assi_rel.selectReqRole()
        self.log.info("************** Selected Assign to only myself Role ***************")

        mrp = ManageRelabelRequestPage(self.driver)
        mrp.clickOnDispatchTab()
        mrp.clickOnManageRelabel()
        add_rel = AddRelabelRequestPage(self.driver)
        add_rel.clickOnDefineSearchCriteria()
        add_rel.clickOnStatus()
        add_rel.clickOnSearch()
        assi_rel.selectRandomRequest()
        assi_rel.clickOnAssign()

    @pytest.fixture(params=TestData_AssignRelabel.test_data_assign)
    def getData_assign(self, request):
        return request.param
