from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

options = Options()
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")
options.add_argument("--disable-gpu")

driver = webdriver.Chrome(
    service=Service(ChromeDriverManager().install()),
    options=options
)

driver.get("file:///C:/Users/Shlok Anand/Desktop/DevOps/task3/index.html")

time.sleep(2)

driver.find_element(By.ID, "name").send_keys("Shlok Anand")
time.sleep(1)

driver.find_element(By.ID, "email").send_keys("shlokanand@gmail.com")
time.sleep(1)

driver.find_element(By.ID, "password").send_keys("123456")
time.sleep(1)

driver.find_element(By.ID, "confirm").send_keys("123456")
time.sleep(1)

driver.find_elements(By.NAME, "gender")[0].click()
time.sleep(1)

driver.find_element(By.TAG_NAME, "button").click()

print("TEST PASSED")

time.sleep(3)

driver.quit()
