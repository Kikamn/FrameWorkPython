# Bikin ke 8
from pom.POM_home import *
from pom.POM_login import *
from helper.action import *
from helper.config import *
# shared_step ini ngebantu agar step login tingal di pangil saja di tiap class meringkas step
def STEP_valid_login(openDriver):
    element_input(openDriver, LOGIN_inputUsername, userName)  # openDriver, pom, text(ambil dari config)
    element_input(openDriver, LOGIN_inputPassword, userPassword)  # openDriver, pom, text(ambil dari config)
    element_click(openDriver, LOGIN_btnLogin) #akan berubah seperti ini jika pake action

    validate_is_display(openDriver,HOME_logoSauce)
