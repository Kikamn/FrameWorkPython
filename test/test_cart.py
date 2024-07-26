# Bikin ke 7
from helper.shared_steps import *
import pytest

@pytest.mark.QaseIO(16)
def test_add_to_cart(openDriver):
    STEP_valid_login(openDriver)
    element_click(openDriver, HOME_atc_item1)
    element_click(openDriver, HOME_atc_item2)
    element_click(openDriver, HOME_atc_item3)

    cart_item = element_get_text(openDriver, HOME_icon_cart)
    #print(cart_item)
    validasi_is_equals(cart_item, "3")

@pytest.mark.QaseIO(17)
def test_remove_to_cart(openDriver): # cara baca code di bawa ini
    STEP_valid_login(openDriver)  # open web sauce dulu dgn kondisi login
    element_click(openDriver, HOME_atc_item1) # Klik add to cart sampe 3x
    element_click(openDriver, HOME_atc_item2)
    element_click(openDriver, HOME_atc_item3)

    cart_item_old = element_get_text(openDriver, HOME_icon_cart) #cek ada 3 di cart
    #print(cart_item)
    validasi_is_equals(cart_item_old, "3") # validasi apakah bnr sudah 3 di cart

    element_click(openDriver, HOME_remove_item1) # Klik remove ke item 1 dan 2
    element_click(openDriver, HOME_remove_item2)

    cart_item_new = element_get_text(openDriver, HOME_icon_cart) #cek ada 1 di cart
    validasi_is_equals(cart_item_new, "1") #Validasi apakah bnr sudah tingal 1

@pytest.mark.QaseIO(18)
def test_add_to_cart_detail_product(openDriver):
    STEP_valid_login(openDriver)
    element_click(openDriver, HOME_detail_product)
    element_click(openDriver, HOME_addtocart)
    cart_item = element_get_text(openDriver, HOME_icon_cart)
    #print(cart_item)
    validasi_is_equals(cart_item, "1")

@pytest.mark.QaseIO(19)
def test_remove_to_cart_detail_product(openDriver):
    STEP_valid_login(openDriver)
    element_click(openDriver, HOME_detail_product)
    element_click(openDriver, HOME_addtocart)
    element_click(openDriver, HOME_btn_remove)


