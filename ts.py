from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.firefox.firefox_profile import FirefoxProfile
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from time import sleep

service = Service()
driver = webdriver.Firefox(service=service)
driver.get('https://www.ts.kg/')

options = Options()
# firefox_profile = FirefoxProfile()
# firefox_profile.set_preference("dom.webdriver.enabled", False)
# firefox_profile.set_preference('useAutomationExtension', False)
options.add_argument('-profile')
options.add_argument('C:/Users/Aibek/AppData/Local/Mozilla/Firefox/Profiles/hy5vywoc.default-release')
options.s()
# options.profile = firefox_profile

tab_to_profile = driver.find_element(By.XPATH, '/html/body/header/nav/div/div[2]/ul[2]/li[5]').click()
tap_to_google = driver.find_element(By.XPATH, '/html/body/header/nav/div/div[2]/ul[2]/li[5]/ul/li[3]/a').click()

sleep(10)
driver.quit()
