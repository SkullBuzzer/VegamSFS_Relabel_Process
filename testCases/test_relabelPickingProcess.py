import pytest

from PageObjects.AddRelabelRequestPage import AddRelabelRequestPage
from PageObjects.AssignRelabelRequestPage import AssignRelabelRequestPage
from PageObjects.LoginPage import LoginPage
from PageObjects.ManageRelabelRequestPage import ManageRelabelRequestPage
from PageObjects.RelabelPickingPage import RelabelPickingPage
from Utilities.BaseClass import BaseClass
from Utilities.customLogger import LogGen
from Utilities.readProperties import ReadConfig


class Test_008_RelabelPickingProcess(BaseClass):
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUsername()
    password = ReadConfig.getPassword()
    log = LogGen.getLogger()

    @pytest.mark.regression
    @pytest.mark.run(order=12)
    def test_pickMaterialForRelabel(self):
        global bin_name
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
        mrp.clickOnManageRelabel()
        assi_rel = AssignRelabelRequestPage(self.driver)
        add_rel = AddRelabelRequestPage(self.driver)
        add_rel.clickOnDefineSearchCriteria()
        add_rel.clickOnStatus()
        assi_rel.selectStatusAssign()
        add_rel.clickOnSearch()
        relID = assi_rel.selectRandomRequest()
        rel_pick = RelabelPickingPage(self.driver)
        material, batch = rel_pick.getMaterial_batch()
        req_qty = rel_pick.getRequestedQty()
        rel_pick.clickOnPalletInfoTab()
        rel_pick.clickOnPalletInfoModule()
        rel_pick.setMaterialCode().send_keys(material)
        rel_pick.setBatch().send_keys(batch)
        rel_pick.clickOnSearch()
        label = rel_pick.getRmLabel()
        self.log.info("**************** RM label captured successfully ***************")
        mrp.clickOnDispatchTab()
        rel_pick.clickOnDispatchMobile()
        rel_pick.clickOnRelabelOption()
        rel_pick.clickOnPickOption()
        rel_pick.selectReqIDForPick(relID)
        rel_pick.clickOnContinue()
        avail_qty, bin_name = rel_pick.scanBinLocation()
        rel_pick.clickOnPick()
        self.log.info("******* Scanned bin location and click on pick button ********")
        rel_pick.scanRmLabel().send_keys(label)
        enter_qty = rel_pick.getQty(float(req_qty), avail_qty)
        rel_pick.enterQty().send_keys(str(enter_qty))
        status = rel_pick.clickOnConfirm(int(req_qty), enter_qty, avail_qty)
        pending_qty = int(req_qty) - enter_qty
        if status == False:
            avail_qty, bin_name = rel_pick.scanBinLocation()
            rel_pick.clickOnPick()
            self.log.info("******* Scanned bin location and click on pick button ********")
            rel_pick.scanRmLabel().send_keys(label)
            rel_pick.enterQty().send_keys(str(pending_qty))
            rel_pick.clickOnConfirm(int(req_qty), enter_qty, avail_qty)
        else:
            pass

        rel_pick.returnPallet().send_keys(bin_name)
        status = rel_pick.clickOnConfirmBtn()
        assert status == True
        rel_pick.clickOnHomeIcon()
        self.log.info("******* Material picked successfully ********")

        rel_pick.clickOnGrid()
        rel_pick.clickOnDispatch()
        mrp.clickOnManageRelabel()
        add_rel.clickOnDefineSearchCriteria()
        add_rel.clickOnStatus()
        rel_pick.selStatusPickingCompleted()
        assi_rel.enterReqID().send_keys(relID)
        add_rel.clickOnSearch()
        act_relID = assi_rel.selectRandomRequest()
        if act_relID == relID:
            assert True
        else:
            assert False
        self.log.info("************ Test Relabel Picking Passed ***************")







