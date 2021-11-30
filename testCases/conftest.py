import pytest
from selenium import webdriver


def pytest_addoption(parser):
    parser.addoption("--browser_name", action='store', default='chrome'
                     )


@pytest.fixture(scope="class")
def setup(request):
    browser_name = request.config.getoption("browser_name")
    if browser_name == "chrome":
        driver = webdriver.Chrome(executable_path="E:\\chromedriver.exe")
    elif browser_name == "firefox":
        driver = webdriver.Firefox(executable_path="E:\\geckodriver.exe")
    driver.maximize_window()
    driver.get_cookies().clear()
    request.cls.driver = driver
    yield
    driver.close()


# *************** HTML Reports ************************
def pytest_configure(config):
    config._metadata['Project Name'] = "VegamSFS_Dispatch"
    config._metadata['Module Name'] = "Dispatch"
    config._metadata['Tester Name'] = 'M Gurubasava'


@pytest.mark.optionalhook
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME", None)
    metadata.pop("Plugins", None)
