import pytest

from PageObjects.AddRelabelRequestPage import AddRelabelRequestPage
from PageObjects.EditDeleteRelabelPage import EditDeleteRelabelPage
from PageObjects.LoginPage import LoginPage
from PageObjects.ManageRelabelRequestPage import ManageRelabelRequestPage
from TestData.testData_Add_New_Relabel import TestData_Add_Relabel
from Utilities.BaseClass import BaseClass
from Utilities.customLogger import LogGen
from Utilities.readProperties import ReadConfig


class Test_002_AddNewRelabelRequest(BaseClass):
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUsername()
    password = ReadConfig.getPassword()
    log = LogGen.getLogger()

    @pytest.mark.run(order=2)
    def test_addNewRelabelRequest(self, getData_add):
        self.log.info("*************** Test_002_AddNewRelabelRequest **************")
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
        add_rel.clickOnAddRelabel()
        add_rel.selectRelabelFrom().send_keys(getData_add['RelabelFrom'])
        self.log.info("************ Adding Relabel From Info **********************")
        add_rel.selectFromKeyCustName()
        add_rel.selectFromCustCode()
        add_rel.setFromCustCode().send_keys(getData_add['FromCustCode'])
        add_rel.selectFromCustName()
        add_rel.setFromMaterialCode().send_keys(getData_add['FromMaterialCode'])
        add_rel.selectFromMaterial()
        add_rel.setFromBatch().send_keys(getData_add['FromBatch'])
        add_rel.setStorageLoc().send_keys(getData_add['StorageLocation'])
        add_rel.setQuantity().send_keys(getData_add['Qty'])
        self.select_drop_down(add_rel.drop_down(), getData_add['Priority'])
        add_rel.setRemarks().send_keys(getData_add['Remarks'])

        self.log.info("*************** Added Relabel From Info ********************")

        self.log.info("*************** Adding Relabel To Info *********************")
        add_rel.selectToRelabel().send_keys(getData_add['RelabelTo'])
        add_rel.selectToKeyCustName()
        add_rel.selectToCustCode().send_keys(getData_add['ToCustCode'])
        add_rel.selectToCustName()
        add_rel.setToMaterialCode().send_keys(getData_add['ToMaterialCode'])
        add_rel.selectToMaterialCode()
        add_rel.setToBatch().send_keys(getData_add['ToBatch'])
        add_rel.setManufactureDate(getData_add['CurrentDate'])
        add_rel.clickOnExpCalendar()
        self.select_drop_down(add_rel.setExpiryMonth(), getData_add['ExpiryMonth'])
        self.select_drop_down(add_rel.setExpiryYear(), getData_add['Year'])
        add_rel.setExpiryDate(getData_add['ExpiryDate'])
        add_rel.setRequestDate(getData_add['CurrentDate'])
        add_rel.enableNewCOA()
        status = add_rel.clickOnSave()
        assert status == True
        self.log.info("************* Test Add new relabel is passed ****************")
        lp.clickOnSignOut()
        lp.clickOnLoginAgain()

    @pytest.mark.run(order=3)
    def test_verifyAddedRelabelRequest(self, getData_add):
        self.log.info("*************** Test verify Added Relabel Request started **************")
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
        add_rel.enterFromMaterialCode().send_keys(getData_add['FromMaterialCode'])
        add_rel.enterToBatchNum().send_keys(getData_add['ToBatch'])
        add_rel.clickOnFromReqCalendar()
        self.select_drop_down(add_rel.setReqFromMonth(), getData_add['CurrentMonth'])
        add_rel.enterRequestDate(getData_add['CurrentDate'])
        add_rel.clickOnSearch()
        status = add_rel.verifyStatus()
        assert status == True
        self.log.info("***** Relabel request added successfully with Requested status *******")
        lp.clickOnSignOut()
        lp.clickOnLoginAgain()

    @pytest.mark.run(order=4)
    def test_copyRelabelRequest(self, getData_copy, getData_add):
        self.driver.implicitly_wait(5)
        self.log.info("*************** Test verify Added Relabel Request started **************")
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
        edit_rel = EditDeleteRelabelPage(self.driver)
        add_rel = AddRelabelRequestPage(self.driver)
        add_rel.clickOnCopyIcon()
        edit_rel.clickOnConfirmButton()
        add_rel.setFromMaterialCode().send_keys(getData_copy['FromMaterial'])
        add_rel.selectFromMaterial()
        add_rel.setToMaterialCode().send_keys(getData_copy['ToMaterial'])
        add_rel.selectToMaterialCode()
        add_rel.setToBatch().send_keys(getData_copy['ToBatch'])
        add_rel.setRequestDate(getData_add['CurrentDate'])
        edit_rel.clickOnSave()
        self.log.info("************ copy of Relabel Request added **************")
        add_rel.clickOnDefineSearchCriteria()
        add_rel.clickOnStatus()
        add_rel.selectStatusRequested()
        add_rel.enterFromMaterialCode().send_keys(getData_copy['FromMaterial'])
        add_rel.enterToBatchNum().send_keys(getData_copy['ToBatch'])
        add_rel.clickOnFromReqCalendar()
        self.select_drop_down(add_rel.setReqFromMonth(), getData_add['CurrentMonth'])
        add_rel.enterRequestDate(getData_add['CurrentDate'])
        add_rel.clickOnSearch()
        status = add_rel.verifyStatus()
        assert status == True
        self.log.info("********** test copy relabel request passed ***********")
        lp.clickOnSignOut()
        lp.clickOnLoginAgain()

    @pytest.fixture(params=TestData_Add_Relabel.test_data_add)
    def getData_add(self, request):
        return request.param

    @pytest.fixture(params=TestData_Add_Relabel.test_data_copy)
    def getData_copy(self, request):
        return request.param
