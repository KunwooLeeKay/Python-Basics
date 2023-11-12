from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

browser = webdriver.Chrome("/Applications/chromedriver")
browser.get("https://realty.daum.net/home/apt/")
elem = browser.find_element_by_xpath("/html/body/div[1]/div[2]/div/div[1]/div/div[2]/div[1]/div[1]/div/div[1]/input")

from selenium.webdriver.common.keys import Keys
elem.send_keys("개포자이")
time.sleep(3)


elem.send_keys(Keys.ENTER)
elem.send_keys(Keys.ENTER)

time.sleep(2)

#초등학교
elem = browser.find_element_by_xpath("/html/body/div[1]/div[2]/div/div[2]/div/div/div[1]/div[2]/div[2]/div/div[14]/div/div[1]/div[2]/div/div[2]/div[1]/div[3]/div[1]/div[1]/div")

# 더보기 있으면 누르고 아님 패스
try:
    browser.find_element_by_xpath("/html/body/div[1]/div[2]/div/div[2]/div/div/div[1]/div[2]/div[2]/div/div[14]/div/div[1]/div[2]/div/div[4]/div/div[1]/div[1]").click()
except:
    pass

time.sleep(1)
school1 = []
number = 3
i = 0
while True:
    try:
        elem = browser.find_element_by_xpath("/html/body/div[1]/div[2]/div/div[2]/div/div/div[1]/div[2]/div[2]/div/div[14]/div/div[1]/div[2]/div/div[2]/div[1]/div["+str(number)+"]/div[1]/div[1]/div")
        school1.append(elem.text)
        number += 2
        i += 1
    except:
        break
print(school1)

# 중학교
elem = browser.find_element_by_xpath("/html/body/div[1]/div[2]/div/div[2]/div/div/div[1]/div[2]/div[2]/div/div[14]/div/div[1]/div[2]/div/div[1]/div[2]/div[2]/div/div[1]")
elem.click()
# elem = WebDriverWait(browser,10).until(ec.presence_of_element_located(By.XPATH, "/html/body/div[1]/div[2]/div/div[2]/div/div/div[1]/div[2]/div[2]/div/div[14]/div/div[1]/div[2]/div/div[2]/div[1]/div[3]/div[1]/div[1]/div"))
try:
    browser.find_element_by_xpath("/html/body/div[1]/div[2]/div/div[2]/div/div/div[1]/div[2]/div[2]/div/div[14]/div/div[1]/div[2]/div/div[4]/div/div[1]/div[1]").click()
except:
    pass
time.sleep(1)

school2 = []
number = 3
i = 0
while True:
    try:
        elem = browser.find_element_by_xpath("/html/body/div[1]/div[2]/div/div[2]/div/div/div[1]/div[2]/div[2]/div/div[14]/div/div[1]/div[2]/div/div[2]/div[1]/div["+str(number)+"]/div[1]/div[1]/div")
        school2.append(elem.text)
        number += 2
        i += 1
    except:
        break
print(school2)


# 고등학교
elem = browser.find_element_by_xpath("/html/body/div[1]/div[2]/div/div[2]/div/div/div[1]/div[2]/div[2]/div/div[14]/div/div[1]/div[2]/div/div[1]/div[2]/div[3]/div")
elem.click()
# elem = WebDriverWait(browser,10).until(ec.presence_of_element_located(By.XPATH, "/html/body/div[1]/div[2]/div/div[2]/div/div/div[1]/div[2]/div[2]/div/div[14]/div/div[1]/div[2]/div/div[2]/div[1]/div[3]/div[1]/div[1]/div"))
try:
    browser.find_element_by_xpath("/html/body/div[1]/div[2]/div/div[2]/div/div/div[1]/div[2]/div[2]/div/div[14]/div/div[1]/div[2]/div/div[4]/div/div[1]/div[1]").click()
except:
    pass
time.sleep(1)

school3 = []
number = 3
i = 0
while True:
    try:
        elem = browser.find_element_by_xpath("/html/body/div[1]/div[2]/div/div[2]/div/div/div[1]/div[2]/div[2]/div/div[14]/div/div[1]/div[2]/div/div[2]/div[1]/div["+str(number)+"]/div[1]/div[1]/div")
        school3.append(elem.text)
        number += 2
        i += 1
    except:
        break
print(school3)