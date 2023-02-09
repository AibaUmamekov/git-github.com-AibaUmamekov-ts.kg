from selenium import webdriver
from selenium.webdriver.common.by import By 
from selenium.webdriver.chrome.options import Options
import time

opts = Options()
user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36'
opts.add_argument('user-agent='+user_agent)

browser = webdriver.Chrome(options=opts)
email = 'email'
password = 'password'

browser.get('https://www.ts.kg/')
check_useragent = browser.execute_script('return navigator.userAgent')
# browser.save_screenshot('2.png')

elem = browser.find_element(By.XPATH, '//*[@id="mobile-navbar-collapse"]/ul[2]/li[5]').click()
google = browser.find_element(By.XPATH, '//*[@id="mobile-navbar-collapse"]/ul[2]/li[5]/ul/li[3]/a').click()

input_email = browser.find_element(By.NAME, 'identifier').send_keys(email) 
next = browser.find_element(By.XPATH, '//*[@id="identifierNext"]/div/button').click()

other = browser.find_element(By.ID, 'view_container').click()
other_click = browser.find_element(By.XPATH, '//*[@id="view_container"]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div/ul/li[2]/div')

input_password = browser.find_element(By.NAME, 'password').send_keys(password)
password_click = browser.find_element(By.ID, 'passwordNext')

# time.sleep(50)
# browser.quit()
