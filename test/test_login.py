#Bikin ke 2
from selenium.webdriver.common.by import By
from pom.POM_home import *
from pom.POM_login import *
from helper.action import *
from helper.config import *
import pytest

@pytest.mark.QaseIO(1)
def test_login_with_valid_username_password(openDriver):
    # print("Test Login")
    #Awal mula
    #openDriver.find_element(LOGIN_inputUsername[0], LOGIN_inputUsername[1]).send_keys("standard_user") # [0] buat Bynya [1] buat valuenya
    #openDriver.find_element(LOGIN_inputPassword[0], LOGIN_inputPassword[1]).send_keys("secret_sauce")
    #openDriver.find_element(LOGIN_btnLogin[0], LOGIN_btnLogin[1]).click() # dari panjang begini
    #openDriver.find_element(HOME_logoSauce[0], HOME_logoSauce[1]).is_displayed()
    # akan jadi seperti ini
    element_input(openDriver, LOGIN_inputUsername, userName)  # openDriver, pom, text(ambil dari config)
    element_input(openDriver, LOGIN_inputPassword, userPassword)  # openDriver, pom, text(ambil dari config)
    element_click(openDriver, LOGIN_btnLogin) #akan berubah seperti ini jika pake action

    validate_is_display(openDriver,HOME_logoSauce)

@pytest.mark.QaseIO(2) #ditambahin saat sudah buat di Qase.io dan mark
def test_login_with_invalid_username_password(openDriver):
    element_input(openDriver, LOGIN_inputUsername, "kika")  # openDriver, pom, text(ambil dari config)
    element_input(openDriver, LOGIN_inputPassword, "Kika123")  # openDriver, pom, text(ambil dari config)
    element_click(openDriver, LOGIN_btnLogin) #akan berubah seperti ini jika pake action

    validate_is_display(openDriver,LOGIN_errorMassage_username_password_wrong)

@pytest.mark.QaseIO(3)
def test_login_with_locked_out_user(openDriver):
    element_input(openDriver, LOGIN_inputUsername, userNameLock)  # openDriver, pom, text(ambil dari config)
    element_input(openDriver, LOGIN_inputPassword, userPassword)  # openDriver, pom, text(ambil dari config)
    element_click(openDriver, LOGIN_btnLogin) #akan berubah seperti ini jika pake action

    validate_is_display(openDriver,LOGIN_errorMassage_Lock)

@pytest.mark.QaseIO(4)
def test_login_blank_username_password(openDriver):
    element_input(openDriver, LOGIN_inputUsername, "")
    element_input(openDriver, LOGIN_inputPassword, "")
    element_click(openDriver, LOGIN_btnLogin)

    validate_is_display(openDriver, LOGIN_errorMassage_blank)

@pytest.mark.QaseIO(5)
def test_login_username_valid_password_blank(openDriver):
    element_input(openDriver, LOGIN_inputUsername, userName)
    element_input(openDriver, LOGIN_inputPassword, "")
    element_click(openDriver, LOGIN_btnLogin)

    validate_is_display(openDriver, LOGIN_errorMassage_password_blank)

@pytest.mark.QaseIO(6)
def test_login_username_blank_password_valid(openDriver):
    element_input(openDriver, LOGIN_inputUsername, "")
    element_input(openDriver, LOGIN_inputPassword, userPassword)
    element_click(openDriver, LOGIN_btnLogin)

    validate_is_display(openDriver, LOGIN_errorMassage_username_blank)



