# Bikin ke 8
from helper.shared_steps import *
import pytest

@pytest.mark.QaseIO(7)
def test_deteail_product(openDriver):
    STEP_valid_login(openDriver)
    element_click(openDriver, HOME_detail_product)
    validate_is_display(openDriver, HOME_btn_back)

@pytest.mark.QaseIO(8)
def test_back_detail_product(openDriver):
    STEP_valid_login(openDriver)
    element_click(openDriver, HOME_detail_product)
    element_click(openDriver, HOME_btn_back)

@pytest.mark.QaseIO(9)
def test_filter_product(openDriver):
    STEP_valid_login(openDriver)
    element_click(openDriver, HOME_filter_product)
    valueAZ = element_get_text(openDriver, HOME_value_AZ)
    validasi_is_equals(valueAZ, "Name (A to Z)")

    valueZA = element_get_text(openDriver, HOME_value_ZA)
    validasi_is_equals(valueZA, "Name (Z to A)")

    valueLowHig = element_get_text(openDriver, HOME_value_LowtoHigh)
    validasi_is_equals(valueLowHig, "Price (low to high)")

    valueHighLow = element_get_text(openDriver, HOME_value_HightoLow)
    validasi_is_equals(valueHighLow, "Price (high to low)")

@pytest.mark.QaseIO(10)
def test_filter_product_ZtoA(openDriver):
    STEP_valid_login(openDriver)
    element_click(openDriver, HOME_filter_product)
    element_click(openDriver, HOME_value_ZA)
    validate_is_display(openDriver, HOME_list_product)

@pytest.mark.QaseIO(11)
def test_burger_menu(openDriver):
    STEP_valid_login(openDriver)
    element_click(openDriver, HOME_burgerMenu)
    validate_is_display(openDriver, HOME_allItem)
    validate_is_display(openDriver, HOME_about)
    validate_is_display(openDriver, HOME_logOut)
    validate_is_display(openDriver, HOME_resetApp)

@pytest.mark.QaseIO(12)
def test_logOut_burgerMenu(openDriver):
    STEP_valid_login(openDriver)
    element_click(openDriver, HOME_burgerMenu)
    element_click(openDriver, HOME_logOut)

@pytest.mark.QaseIO(13)
def test_sosmed_footer_twitter(openDriver):
    STEP_valid_login(openDriver)
    element_click(openDriver, HOME_footer_twitter)
    valodasi_url(openDriver, url_twitter)

@pytest.mark.QaseIO(14)
def test_sosmed_footer_FB(openDriver):
    STEP_valid_login(openDriver)
    element_click(openDriver, HOME_footer_FB)
    valodasi_url(openDriver, url_fb)

@pytest.mark.QaseIO(15)
def test_sosmed_footer_linkedin(openDriver):
    STEP_valid_login(openDriver)
    element_click(openDriver, HOME_footer_LN)
    valodasi_url(openDriver, url_ln)


