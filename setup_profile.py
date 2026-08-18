import time 
from seleniumbase import Driver

from config import FORM_URL, CHROME_PROFILE_DIR


driver = Driver(
    uc = True,
    user_data_dir = CHROME_PROFILE_DIR,
    chromium_arg = "--no-sandbox, --disable-dev-shm-usage",
    do_not_track = True
)


try:
    # Open the form
    driver.get(FORM_URL)

    # SIGN IN using ur profile under 60 sec or add more if u like
    time.sleep(120) # (waits for 60 sec)

finally:
    # Closes the browser
    driver.quit() # prevent ghost processes