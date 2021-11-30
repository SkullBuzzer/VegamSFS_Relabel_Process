import time

import pytest

from PageObjects.DownloadUploadPage import DownloadUploadPage
from PageObjects.LoginPage import LoginPage
from PageObjects.ManageRelabelRequestPage import ManageRelabelRequestPage
from Utilities.BaseClass import BaseClass
from Utilities.customLogger import LogGen
from Utilities.readProperties import ReadConfig


class Test_006_DownloadUpload(BaseClass):
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUsername()
    password = ReadConfig.getPassword()
    log = LogGen.getLogger()

    @pytest.mark.run(order=6)
    def test_downloadTemplate(self):
        self.log.info("************** Test_006_DownloadUpload **************")
        self.driver.get(self.baseURL)
        lp = LoginPage(self.driver)
        lp.setUserName().send_keys(self.username)
        lp.setPassword().send_keys(self.password)
        lp.clickOnLogin()
        self.log.info("************** Login Successful *****************")
        mrp = ManageRelabelRequestPage(self.driver)
        mrp.clickOnDispatchTab()
        mrp.clickOnManageRelabel()
        self.log.info("******* Accessed manage Relabel Request Page *******")
        dup = DownloadUploadPage(self.driver)
        dup.clickOnDownloadUpload()
        dup.clickOnDownloadTemp()
        self.log.info("******* Template downloaded successfully **********")
        lp.clickOnSignOut()
        lp.clickOnLoginAgain()

    @pytest.mark.run(order=7)
    def test_uploadTemplate(self):
        self.log.info("************** Test_006_DownloadUpload **************")
        self.driver.get(self.baseURL)
        lp = LoginPage(self.driver)
        lp.setUserName().send_keys(self.username)
        lp.setPassword().send_keys(self.password)
        lp.clickOnLogin()
        self.log.info("************** Login Successful *****************")
        mrp = ManageRelabelRequestPage(self.driver)
        mrp.clickOnDispatchTab()
        mrp.clickOnManageRelabel()
        self.log.info("******* Accessed manage Relabel Request Page *******")
        dup = DownloadUploadPage(self.driver)
        dup.clickOnDownloadUpload()
        dup.clickOnUploadTemp()
        self.driver.find_element_by_xpath("//input[@id='ContentPlaceHolder1_uploadFile']").send_keys("C:\\Users\\Dell"
                                                                                                     "\\OneDrive"
                                                                                                     "\\Desktop"
                                                                                                     "\\ManageRelabel_Template.xlsx")
        time.sleep(15)
        self.log.info("******* test upload template is passed **********")
        lp.clickOnSignOut()
        lp.clickOnLoginAgain()

    @pytest.mark.run(order=8)
    def test_downloadInfo(self):
        self.log.info("************** Test_006_DownloadUpload **************")
        self.driver.get(self.baseURL)
        lp = LoginPage(self.driver)
        lp.setUserName().send_keys(self.username)
        lp.setPassword().send_keys(self.password)
        lp.clickOnLogin()
        self.log.info("************** Login Successful *****************")
        mrp = ManageRelabelRequestPage(self.driver)
        mrp.clickOnDispatchTab()
        mrp.clickOnManageRelabel()
        self.log.info("******* Accessed manage Relabel Request Page *******")
        dup = DownloadUploadPage(self.driver)
        dup.clickOnDownloadUpload()
        dup.clickOnDownloadInfo()
        self.log.info("******* test download info is passed **********")
        lp.clickOnSignOut()
        lp.clickOnLoginAgain()
