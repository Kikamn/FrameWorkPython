#Bikin ke 1
import json
import time
import pytest
from selenium.webdriver.chrome.options import  Options
from selenium import webdriver
from helper.config import *
from helper.test_management_integration import *


#def pytest_html_report_name(report): # fungsi nama report di html
#    report.title = "Report Selenium Python"

@pytest.fixture()
def openDriver():
    o = Options()
    o.add_argument("--headless")
    o.add_argument("--no-sandbox") #Bukan staging
    o.add_argument("--disable-dev-shm-usage")
    o.add_argument("--remote-allow-origins=*") #ini dapat di remote
    o.add_argument("--window-size=190,1080")
    o.add_argument("--disable-web-security")

    driver = webdriver.Chrome(options=o)
    driver.maximize_window()
    driver.implicitly_wait(15)
    return driver


@pytest.fixture(scope='function', autouse=True)
def hook(request, openDriver):
    #print("Before Tes")
    #openDriver.get("https://www.saucedemo.com/") #open web sesuai link
    openDriver.get(url_web) #ngambil url dari config helper jangan lupa di import dulu
    get_error = request.session.testsfailed

    yield
    #print("After Test")
    markers = request.node.get_closest_marker("QaseIO")
    test_result = request.session.testsfailed - get_error
    case_id = str(markers.args[0])

    if test_result == 0:
        push_result(case_id, "passed")
    else:
        push_result(case_id, "failed")
    #print(f"Hasil Testing : {test_result}")
    #print(f"custom marker : {markers.args[0]}")
    openDriver.quit() #fungsinya habis buka nnti di tutup

@pytest.fixture(scope='session', autouse=True)
def suite(request):
    #print("Before Tes")

    yield
    #print("After Test")

