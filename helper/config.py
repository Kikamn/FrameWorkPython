#helper untuk nyimpen url" di config
# Bikin ke 3
# ========================================== URL ================================================
import os

url_web = "https://www.saucedemo.com/"
url_twitter = "https://x.com/saucelabs"
url_fb = "https://www.facebook.com/saucelabs"
url_ln = "https://www.linkedin.com/company/sauce-labs/"

# =========================================== INPUTAN LOGIN =======================================
userName = "standard_user"
userPassword = "secret_sauce"
userNameLock = "locked_out_user"

# ========================================= KEY API =================================================
#TOKEN_QASE_IO = "996136e88f026a900b4c935b1ad57d907e808393b691f2b35fc643c26679225c"
TOKEN_QASE_IO = os.environ.get("QASE_IO_TOKEN") # setelah di set di git hub
host_QaseIO = "https://api.qase.io/v1/result/"
project_ID = "FWP"
test_run_id = "1"