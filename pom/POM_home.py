# Bikin ke 5

from selenium.webdriver.common.by import By

HOME_logoSauce= [By.XPATH, "//*[@class='app_logo']"] #nama ini di ambil dari halaman apa awalannya
HOME_atc_item1 = [By.XPATH, "(//*[text()='Add to cart'])[1]"]
HOME_atc_item2 = [By.XPATH, "(//*[text()='Add to cart'])[2]"]
HOME_atc_item3 = [By.XPATH, "(//*[text()='Add to cart'])[3]"]

HOME_remove_item1 = [By.XPATH, "(//*[text()='Remove'])[1]"]
HOME_remove_item2 = [By.XPATH, "(//*[text()='Remove'])[2]"]

HOME_icon_cart = [By.XPATH, "//*[@data-test='shopping-cart-badge']"]
# DETAIL PRODUCT
HOME_detail_product = [By.XPATH, "//*[@data-test='item-4-title-link']"]
HOME_addtocart = [By.ID, "add-to-cart"]
HOME_btn_remove = [By.NAME, "remove"]
HOME_btn_back = [By.ID, "back-to-products"]
# FILTER PRODUCT
HOME_filter_product = [By.XPATH, "//*[@data-test='product-sort-container']"]
HOME_value_AZ = [By.XPATH, "//*[@value='az']"]
HOME_value_ZA = [By.XPATH, "//*[@value='za']"]
HOME_value_LowtoHigh = [By.XPATH, "//*[@value='lohi']"]
HOME_value_HightoLow = [By.XPATH, "//*[@value='hilo']"]
HOME_list_product = [By.XPATH, "//*[@id='item_3_title_link']"]
#BURGER MENU
HOME_burgerMenu = [By.ID, "react-burger-menu-btn"]
HOME_allItem = [By.ID, "inventory_sidebar_link"]
HOME_about = [By.ID, "about_sidebar_link"]
HOME_logOut = [By.XPATH, "//*[@data-test='logout-sidebar-link']"]
HOME_resetApp = [By.ID, "reset_sidebar_link"]
#FOOTER
HOME_footer_twitter = [By.XPATH, "//*[@data-test='social-twitter']"]
HOME_footer_FB = [By.XPATH, "//*[@data-test='social-facebook']"]
HOME_footer_LN = [By.XPATH, "//*[@data-test='social-linkedin']"]