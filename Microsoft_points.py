from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import random

Searches = ["MAKE A LIST"]

driver = webdriver.Edge()

driver.get("https://www.bing.com/")
sleep(3)
try:
    driver.find_element(by=By.XPATH, value='//*[@id="id_l"]').click()
    sleep(3)
    driver.find_element(by=By.XPATH, value='//*[@id="hb_s"]').click()
    sleep(3)
    driver.find_element(by=By.XPATH, value='//*[@id="i0116"]').send_keys("EMAIL")
    sleep(3)
    driver.find_element(by=By.XPATH, value='//*[@id="idSIButton9"]').click()
    sleep(3)
    driver.find_element(by=By.XPATH, value='//*[@id="msaTile"]/div/div[2]').click()
    sleep(3)
    driver.find_element(by=By.XPATH, value='//*[@id="i0118"]').send_keys("PASSWORD")
    sleep(3)
    driver.find_element(by=By.XPATH, value='//*[@id="idSIButton9"]').click()
    sleep(3)
    driver.find_element(by=By.XPATH, value='//*[@id="idSIButton9"]').click()
    sleep(3)
except NoSuchElementException:
    pass
count1 = 40
while count1 > 0:
    Send1 = Searches.pop(random.randint(0, len(Searches)-1))
    sleep(3)
    driver.find_element(by=By.XPATH, value='//*[@id="sb_form_q"]').send_keys(Send1, Keys.ENTER)
    sleep(3)
    driver.find_element(by=By.XPATH, value='//*[@id="sb_form_q"]').clear()
    count1 -= 1



driver.quit()