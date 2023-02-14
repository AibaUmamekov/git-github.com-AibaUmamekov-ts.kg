import undetected_chromedriver as uc
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from time import sleep

email = '@@@@@@@@@@@@@@@@'
password = '############'


driver = uc.Chrome()
wait = WebDriverWait(driver, 20)
driver.get('https://accounts.google.com/v3/signin/identifier?dsh=S84008425%3A1676387120552879&continue=https%3A%2F%2Fwww.google.com%3Fhl%3Dru&ec=GAlA8wE&hl=ru&flowName=GlifWebSignIn&flowEntry=AddSession')


wait.until(EC.visibility_of_element_located((By.NAME, 'identifier'))).send_keys(email)
EmailNext = driver.find_element(By.XPATH, '//*[@id="identifierNext"]/div/button').click()

wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="password"]/div[1]/div/div[1]/input'))).send_keys(password)
PasswdNext = driver.find_element(By.XPATH, '//*[@id="passwordNext"]/div/button').click()

driver.get('http://www.ts.kg/')

driver.find_element(By.XPATH, '//*[@id="mobile-navbar-collapse"]/ul[2]/li[5]').click()
driver.find_element(By.XPATH, '//*[@id="mobile-navbar-collapse"]/ul[2]/li[5]/ul/li[3]/a').click()

driver.find_element(By.XPATH, '//*[@id="mobile-navbar-collapse"]/ul[2]/li[5]/div/input').send_keys('The last of us')

sleep(100)

# time.sleep(50)
# browser.quit()
