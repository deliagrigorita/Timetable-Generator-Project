from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


email = "deliagrigorita@yahoo.com"
password = "1234"

urls = ['http://127.0.0.1:8000/auth/']

chrome_options = webdriver.ChromeOptions()

chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])
chrome_options.add_argument('--log-level=3')

driver = webdriver.Chrome(options=chrome_options)

wait = WebDriverWait(driver, 10)  

try:
    for url in urls:
        driver.get(url)

        email_field = wait.until(EC.presence_of_element_located((By.ID, "id_email")))
        email_field.send_keys(email)

        password_field = driver.find_element(By.ID, "id_password")
        password_field.send_keys(password)

        login_button = driver.find_element(By.XPATH, "//button[text()='Login']")
        login_button.click()

    print("Before wait - Current URL:", driver.current_url)
    wait.until(EC.url_contains('http://127.0.0.1:8000'))  
    print("After wait - Current URL:", driver.current_url)

    print("Login Successful")

except Exception as e:
    import traceback
    traceback.print_exc()

finally:
    driver.quit()