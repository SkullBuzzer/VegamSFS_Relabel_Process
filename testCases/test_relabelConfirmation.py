import pytest

from PageObjects.AddRelabelRequestPage import AddRelabelRequestPage
from PageObjects.AssignRelabelRequestPage import AssignRelabelRequestPage
from PageObjects.LoginPage import LoginPage
from PageObjects.ManageRelabelRequestPage import ManageRelabelRequestPage
from PageObjects.RelabelConfirmPage import RelabelConfirmPage
from PageObjects.RelabelPickingPage import RelabelPickingPage
from Utilities.BaseClass import BaseClass
from Utilities.customLogger import LogGen
from Utilities.readProperties import ReadConfig


class Test_009_RelabelConfirm(BaseClass):
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUsername()
    password = ReadConfig.getPassword()
    log = LogGen.getLogger()

    @pytest.mark.run(order=13)
    def test_printRelabel(self):
        self.driver.implicitly_wait(10)
        self.log.info("************ Test_009_RelabelConfirm ************")
        self.log.info("******** test relabel printing started *********")
        self.driver.get(self.baseURL)
        lp = LoginPage(self.driver)
        lp.setUserName().send_keys(self.username)
        lp.setPassword().send_keys(self.password)
        lp.clickOnLogin()
        self.log.info("***************** Login Successful *****************")
        mrp = ManageRelabelRequestPage(self.driver)
        mrp.clickOnDispatchTab()
        mrp.clickOnManageRelabel()
        add_rel = AddRelabelRequestPage(self.driver)
        add_rel.clickOnDefineSearchCriteria()
        add_rel.clickOnStatus()
        rel_pick = RelabelPickingPage(self.driver)
        rel_pick.selStatusPickingCompleted()
        add_rel.clickOnSearch()
        ass_rel = AssignRelabelRequestPage(self.driver)
        relID = ass_rel.selectRandomRequest()
        rel_conf = RelabelConfirmPage(self.driver)
        packsize = rel_conf.getPackSize()
        req_qty = rel_pick.getRequestedQty()
        mrp.clickOnDispatchTab()
        rel_pick.clickOnDispatchMobile()
        rel_pick.clickOnRelabelOption()
        rel_conf.clickOnRelabelOption()
        rel_conf.selectReqIDRelabelConf(relID)
        rel_conf.clickOnPrintLabel()
        rel_conf.enterQty(int(req_qty), int(packsize))
        rel_conf.printLabel()
        status = rel_conf.confirmMsg()
        assert status == True
        rel_conf.clickOnOk()
        self.log.info("************* test relabel printing passed ***********")
        rel_pick.clickOnGrid()
        rel_pick.clickOnDispatch()
        lp.clickOnSignOut()
        lp.clickOnLoginAgain()

    @pytest.mark.run(order=14)
    def test_relabelConfirm(self):
        self.driver.implicitly_wait(10)
        self.log.info("******** test relabel confirm started *********")
        self.driver.get(self.baseURL)
        lp = LoginPage(self.driver)
        lp.setUserName().send_keys(self.username)
        lp.setPassword().send_keys(self.password)
        lp.clickOnLogin()
        self.log.info("***************** Login Successful *****************")
        mrp = ManageRelabelRequestPage(self.driver)
        mrp.clickOnDispatchTab()
        mrp.clickOnManageRelabel()
        add_rel = AddRelabelRequestPage(self.driver)
        add_rel.clickOnDefineSearchCriteria()
        add_rel.clickOnStatus()
        rel_pick = RelabelPickingPage(self.driver)
        rel_pick.selStatusPickingCompleted()
        add_rel.clickOnSearch()
        ass_rel = AssignRelabelRequestPage(self.driver)
        relID = ass_rel.selectRandomRequest()
        rel_conf = RelabelConfirmPage(self.driver)
        toMaterial, toBatch = rel_conf.getToMaterial_Batch()
        fromMat, fromBatch = rel_pick.getMaterial_batch()
        packsize = rel_conf.getPackSize()
        req_qty = rel_pick.getRequestedQty()
        rel_conf.clickOnPalletInfo()
        rel_pick.clickOnPalletInfoModule()
        rel_pick.setMaterialCode().send_keys(fromMat)
        rel_pick.setBatch().send_keys(fromBatch)
        rel_pick.clickOnSearch()
        fromLabel = rel_pick.getRmLabel()
        self.driver.refresh()
        rel_pick.setMaterialCode().send_keys(toMaterial)
        rel_pick.setBatch().send_keys(toBatch)
        rel_pick.clickOnSearch()
        ToLabel = rel_pick.getRmLabel()
        mrp.clickOnDispatchTab()
        rel_pick.clickOnDispatchMobile()
        rel_pick.clickOnRelabelOption()
        rel_conf.clickOnRelabelOption()
        rel_conf.selectReqIDRelabelConf(relID)
        rel_conf.clickOnContinue()
        rel_conf.scanFromLabel().send_keys(fromLabel)
        rel_conf.scanToLabel().send_keys(ToLabel)
        rel_conf.clickOnConfirm()
        status = rel_conf.verifyRecord()
        assert status == True
        rel_conf.clickOnOk()
        rel_pick.clickOnGrid()
        rel_pick.clickOnDispatch()
        mrp.clickOnManageRelabel()
        add_rel.clickOnDefineSearchCriteria()
        add_rel.clickOnStatus()
        rel_conf.selectRelabelCompleted()
        ass_rel.enterReqID().send_keys(relID)
        add_rel.clickOnSearch()
        act_relID = ass_rel.selectRandomRequest()
        if act_relID == relID:
            assert True
        else:
            assert False
        self.log.info("********* test relabel confirm passed ************")



























