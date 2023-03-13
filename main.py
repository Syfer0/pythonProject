from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# open a Chrome browser
driver = webdriver.Chrome()

# navigate to Instagram
driver.get("https://www.instagram.com")

# Enter your username and password here
username = "Epic_pubg17"
password = "pubg@123456"

# Navigate to the login page
driver.get("https://www.instagram.com/accounts/login/")

# Wait for the username input field to become visible
username_field = WebDriverWait(driver, 30).until(
    EC.visibility_of_element_located((By.CSS_SELECTOR, "input[name='username']"))
)

# Enter the username and password
username_field.send_keys(username)
password_field = driver.find_element(By.CSS_SELECTOR, "input[name='password']")
password_field.send_keys(password)

# Click the login button
login_button = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
login_button.click()

# Wait for the home page to load
WebDriverWait(driver, 5).until(
    EC.url_contains("https://www.instagram.com/")
)
# wait for page to load
time.sleep(5)

# dismiss notifications popup
not_now_button = driver.find_element(By.XPATH, "//button[contains(.,'Not Now')]")
not_now_button.click()

new_post_button = WebDriverWait(driver, 50).until(EC.presence_of_element_located((By.XPATH, "*[@id=\"mount_0_0_4s\"]/div/div/div[1]/div/div/div/div[1]/div[1]/div[1]/div/div/div/div/div[2]/div[7]/div/div/a/div")))
new_post_button.click()

# navigate to new post page
new_post_button = driver.find_element(By.XPATH, "*[@id=\"mount_0_0_4s\"]/div/div/div[1]/div/div/div/div[1]/div[1]/div[1]/div/div/div/div/div[2]/div[7]/div/div/a/div")
new_post_button.click()
photo_upload = driver.find_element(By.XPATH, "//input[@type='file']")
photo_upload.send_keys("C:\\Users\\arman\\Downloads\\profile\\rj.jpg")

time.sleep(30)

# add caption and post
next_button = driver.find_element(By.XPATH, "//button[contains(.,'Next')]")
next_button.click()
caption_field = driver.find_element(By.XPATH, "//textarea[@aria-label='Write a caption…']")
caption_field.send_keys("Hello, this is an automated post using Selenium with Python!")
share_button = driver.find_element(By.XPATH, "//button[contains(.,'Share')]")
share_button.click()

# wait for post to be published
time.sleep(5)

# close the browser
driver.quit()





