# Bikin ke 6
from assertpy import assert_that
#============================================= ACTION ===================================================
def element_click(openDriver, pom):
    openDriver.find_element(pom[0], pom[1]).click() # ambil element dri test_login di ubah jadi begini

def element_input(openDriver, pom, text):
    openDriver.find_element(pom[0], pom[1]).send_keys(text) # ambil element dri test_login di ubah jadi begini

#============================================= VALIDATION ===================================================

def validate_is_display(openDriver, pom):
    openDriver.find_element(pom[0], pom[1]).is_displayed()

#============================================= CART ===================================================
def element_get_text (openDriver, pom): #UNTUK NAMPILIN ANGKA DARI CART
   return openDriver.find_element(pom[0], pom[1]).text

def validasi_is_equals(text1, text2):
    assert_that(text1).is_equal_to(text2)

def valodasi_url(openDriver, text):
    openDriver.get(text)