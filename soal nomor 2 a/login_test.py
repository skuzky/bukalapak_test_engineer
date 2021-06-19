from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait

browser = webdriver.Chrome('E:/selenium/chromedriver.exe')

browser.get("https://accounts.bukalapak.com/login")

email = browser.find_element_by_id("user_session_username")

email.send_keys("karamello977@gmail.com")

password = browser.find_element_by_id("user_session_password")

password.send_keys("samsung12@")

submit = browser.find_element_by_xpath("//button[@name='commit']")

submit.click()

wait = WebDriverWait(browser, 5)
page_title = browser.title
print (page_title)