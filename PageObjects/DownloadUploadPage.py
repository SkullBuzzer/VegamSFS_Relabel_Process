import time

from selenium.webdriver.common.by import By


class DownloadUploadPage:
    lnkDownloadUpload = (By.XPATH, "//div[@class='down-up-div mr-3']")
    btnDownloadTemp = (By.XPATH, "//button[@id='btnDownloadTemplate']")
    btnUploadTemp = (By.XPATH, "//button[@id='ContentPlaceHolder1_btnUploadData']")
    btnDownloadInfo = (By.XPATH, "//button[@id='btnDownloadData']")

    def __init__(self, driver):
        self.driver = driver

    def clickOnDownloadUpload(self):
        self.driver.find_element(*self.lnkDownloadUpload).click()

    def clickOnDownloadTemp(self):
        self.driver.find_element(*self.btnDownloadTemp).click()
        time.sleep(15)

    def clickOnUploadTemp(self):
        self.driver.find_element(*self.btnUploadTemp).click()

    def clickOnDownloadInfo(self):
        self.driver.find_element(*self.btnDownloadInfo).click()
        time.sleep(15)


