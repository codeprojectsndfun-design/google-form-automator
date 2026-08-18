

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from seleniumbase import Driver


from faker import Faker
import random
import time
import traceback


import config



driver = Driver (
        uc = True,
        user_data_dir = config.CHROME_PROFILE_DIR, # Injectng Profile
        chromium_arg = "--no-sandbox, --disable-dev-shm-usage",
        do_not_track = True
        )

driver.options.detach = True




fake = Faker('en_In')
wait = WebDriverWait(driver, 10)

# Form Url
FORM_URL = config.FORM_URL
TOTAL_SUBMISSIONS = config.TOTAL_SUBMISSIONS
USER_EMAIL = config.USER_EMAIL
INTERVIEWER_NAME = config.INTERVIEWER_NAME
current_count = 0

while current_count < TOTAL_SUBMISSIONS:
        try:        

                driver.default_get(FORM_URL)
                print(f"Submission starting {current_count + 1} of {TOTAL_SUBMISSIONS}")
                

                # Email & Interview
                email_input = wait.until(EC.presence_of_element_located((By.XPATH, "//input[@type='email']")))
                email_input.send_keys(USER_EMAIL)

                dropdown = wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@role='listbox']")))
                dropdown.click()
                time.sleep(random.uniform(0.5, 1.5))

                interviewer_xpath = f"//div[@role='option' and contains(., '{INTERVIEWER_NAME}')]"
                interviewer_option = wait.until(EC.element_to_be_clickable((By.XPATH, interviewer_xpath)))
                interviewer_option.click()
                time.sleep(random.uniform(0.5, 1.5))

                Next_btn = driver.find_element(By.XPATH, "//span[text()='Next']")
                Next_btn.click()

                # Next Section

                # Wait till 1st question(listitem) loads
                wait.until(EC.presence_of_element_located((By.XPATH, "//div[@role='listitem']")))
                time.sleep(random.uniform(0.5, 1.5))

                # Question that contains name
                name_xpath = "//div[@role='listitem'][contains(., 'Name')]//input[@type='text']"
                Name_input = driver.find_element(By.XPATH, name_xpath) 

                # assign gender at random + same gen name
                assigned_gender = random.choice(['Male','Female'])

                if assigned_gender == "Male":
                        Name_input.send_keys(fake.name_male())
                else:
                        Name_input.send_keys(fake.name_female())

                time.sleep(random.uniform(0.5, 1.5))


                # Random Ans for this radio btn
                all_questions = driver.find_elements(By.XPATH, "//div[@role='listitem']")

                # So not to load questions from next section
                questions = [q for q in all_questions if q.is_displayed()] 
                
                for question in questions:
                        # select btns
                        radios = question.find_elements(By.XPATH, ".//div[@role='radio']")
                        visible_radios = [r for r in radios if r.is_displayed()]

                        if visible_radios:

                                # check if its gender Q then use assigned gender
                                question_text = question.text.lower()

                                if "gender" == question_text:

                                        # select the assigned gender
                                        for radio in visible_radios:
                                                if radio.get_attribute("data-value") == assigned_gender:
                                                        radio.click()
                                                        break # break inner loop and move to next Q

                                # select randomn ans for other Qs
                                else:
                                        random.choice(visible_radios).click()
                                        time.sleep(random.uniform(0.1, 0.2))    

                # No. of Family members
                number_xpath = "//div[@role='listitem'][contains(., 'number')]//input[@type='text']"            
                number_input = driver.find_element(By.XPATH, number_xpath)
                number_input.send_keys(str(random.randint(3, 6)))

                Next_btn = driver.find_element(By.XPATH, "//span[text()='Next']")
                Next_btn.click()

                # Next section
                wait.until(EC.presence_of_element_located((By.XPATH, "//div[@role='listitem']")))
                time.sleep(random.uniform(0.5, 1.5))

                all_questions = driver.find_elements(By.XPATH, "//div[@role='listitem']")

                questions = [q for q in all_questions if q.is_displayed()]

                for question in questions:
                        radios = question.find_elements(By.XPATH, ".//div[@role='radio']")
                        visible_radios = [r for r in radios if r.is_displayed()]

                        if radios:
                                random.choice(visible_radios).click()
                                time.sleep(random.uniform(0.1, 0.2))

                 
                
                

                Submit_btn = driver.find_element(By.XPATH, "//span[text()='Submit']")
                Submit_btn.click()

                # Wait and check if res + captcha is submitted
                while True:
                        try:
                                driver.find_element(By.XPATH, "//a[text()='Submit another response']")
                                break
                        except:
                                time.sleep(0.5)
                
                current_count += 1

                # WAIT FOR CONFIRM Pg
                if current_count < TOTAL_SUBMISSIONS - 1:                        
                        link_xpath = "//a[text()='Submit another response']"
                        another_response_link = wait.until(EC.element_to_be_clickable((By.XPATH, link_xpath)))

                        another_response_link.click()

                        time.sleep(random.uniform(0.5, 1.5))

                

        



        except Exception as e:
                print(e)
                traceback.print_exc()

                print("PAUSED DUE TO ERROR")
        
driver.quit()