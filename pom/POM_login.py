# POM : Page Object Model
# Bikin ke 4
from selenium.webdriver.common.by import By

LOGIN_logoSauce = [By.XPATH, "//*[@class='login_logo']"]
LOGIN_inputUsername = [By.ID, "user-name"] #nama ini di ambil dari halaman apa awalannya
LOGIN_inputPassword = [By.ID, "password"]
LOGIN_btnLogin = [By.ID, "login-button"]

# ================================================== ERROR MASSAGE ==================================================
LOGIN_errorMassage_username_password_wrong = [By.XPATH, "//h3[contains(text(),'Username and password do not match')]"] #cari di selectorsHub
LOGIN_errorMassage_Lock = [By.XPATH, "//h3[contains(text(),'has been locked out')]"]
LOGIN_errorMassage_blank = [By.XPATH, "//h3[contains(text(),'Username is required')]"]
LOGIN_errorMassage_password_blank = [By.XPATH, "//h3[contains(text(),'Password is required')]"]
LOGIN_errorMassage_username_blank = [By.XPATH, "//h3[contains(text(),'Username is required')]"]