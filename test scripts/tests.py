# Before to run the scripts:

"""Install Selenium in the terminal: 
pip install selenium
 
Download Chrome driver:
 https://chromedriver.chromium.org/downloads """


# 1. Login credentials test: 

from selenium import webdriver 
from selenium.webdriver.common.by import By 
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC 
import time

# Configure Chrome driver 

driver = webdriver.Chrome() 

# Load the login page

driver.get('http://localhost:3000/login')  

# Enter valid username and valid password 

username = 'testuser' 
password = 'password' 
# Find username and password fields and fill in the data

username_field = WebDriverWait(driver, 10).until( 
    EC.presence_of_element_located((By.ID, 'username')) 
) 
username_field.send_keys(username) 
password_field = WebDriverWait(driver, 10).until( 
    EC.presence_of_element_located((By.ID, 'password')) 
) 
password_field.send_keys(password) 

# Find the login button and click

login_button = WebDriverWait(driver, 10).until( 
    EC.element_to_be_clickable((By.TAG_NAME, 'button')) 
) 
login_button.click() 

# Verify if the user has been redirected to the dashboard

try: 
    WebDriverWait(driver, 10).until( 
        EC.url_contains('/dashboard')
    ) 
    print('User redirected to dashboard successfully') 
except: 
    print('User has not been redirected to the dashboard') 

# Pause to see the result 

time.sleep(2) 

# Close the driver

driver.quit() 
 

###########################################################


# 2. Empty fields validation test: 

from selenium import webdriver 
from selenium.webdriver.common.by import By 
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC 
import time 

# Configure Chrome driver

driver = webdriver.Chrome() 

# Load the login page

driver.get('http://localhost:3000/login')

# Find the login button and click without entering credentials

login_button = WebDriverWait(driver, 10).until( 
    EC.element_to_be_clickable((By.TAG_NAME, 'button')) 
) 
login_button.click() 

# Verify if an error message appears

try: 
    error_message = WebDriverWait(driver, 10).until( 
        EC.presence_of_element_located((By.TAG_NAME, 'p')) 
    ).text 
    print(f'Error message: {error_message}') 
    assert 'Login failed' in error_message 
except: 
    print('No error message found.') 

# Pause to see the result 

time.sleep(2)  

#Close the driver

driver.quit() 
 

#############################################################


# 3. Incorrect credentials validation test: 

from selenium import webdriver 
from selenium.webdriver.common.by import By 
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC 
import time 

# Configure Chrome driver

driver = webdriver.Chrome() 

# Load the login page

driver.get('http://localhost:3000/login')

# Enter an incorrect username and password

username = 'invalid_user' 
password = 'invalid_password' 

# Find username and password fields and fill in the data

username_field = WebDriverWait(driver, 10).until( 
    EC.presence_of_element_located((By.ID, 'username')) 
) 
username_field.send_keys(username) 
password_field = WebDriverWait(driver, 10).until( 
    EC.presence_of_element_located((By.ID, 'password')) 
) 
password_field.send_keys(password) 

# Find the login button and click

login_button = WebDriverWait(driver, 10).until( 
    EC.element_to_be_clickable((By.TAG_NAME, 'button')) 
) 
login_button.click() 

# Verify if an error message appears

try: 
    error_message = WebDriverWait(driver, 10).until( 
        EC.presence_of_element_located((By.TAG_NAME, 'p')) 
    ).text 
    print(f'Error message: {error_message}') 
    assert 'Login failed' in error_message 
except: 
    print('No error message found.') 

# Pause to see the result

time.sleep(2) 

# Close the driver

driver.quit() 
 
