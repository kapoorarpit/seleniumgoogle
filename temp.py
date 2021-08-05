from selenium import webdriver
from selenium.webdriver.common import service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time 

options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
#driver = webdriver.Chrome(options=options)
path = "C:\Program Files (x86)\chromedriver.exe"
driver =webdriver.Chrome(path)


url = "https://www.google.com/search?q=restaurants+in+bareilly&oq=restaurants+in+bareilly&aqs=chrome..69i57.22434j0j9&sourceid=chrome&ie=UTF-8"
driver.get(url)
 

view_all = WebDriverWait(driver, 90).until(
    EC.presence_of_element_located((By.PARTIAL_LINK_TEXT, "View all"))
)
view_all.click()
time.sleep(5)
main= driver.find_element_by_xpath("//*[@id='rl_ist0']/div[1]")
time.sleep(5)
name = driver.find_elements_by_xpath("//div[@jscontroller='AtSb']")
for i in name:
    temp= main.find_element_by_partial_link_text(i.text).click()
    #temp.click()
    time.sleep(2)

    title= driver.find_element_by_xpath("//h2[@data-attrid='title']")
    try:
        print("Name : "+title.text)
    except:
        continue
    print("")
    try:
        address= driver.find_element_by_xpath(" //div[@data-dtype='d3ifr' and @data-local-attribute='d3adr']")
        print(address.text)
    except:
        print("address : N/A" )
    print("")
    try:
        rating = driver.find_element_by_xpath("//div[@data-md='205' and @lang='en-IN']")
        newstr = rating.text.rstrip()
        print("rating and reviews : ", end="")
        rez = []
        for sub in newstr:
            rez.append(sub.replace("\n", " "))
        for j in rez:
            print(j, end="")
    except:
        print("ratings : N/A")
    print("")
    print("")
    try:
        service = driver.find_element_by_xpath("//c-wiz[@jsrenderer='KfXAkb' and @jsmodel='hc6Ubd']")
        print("service : "+service.text)
    except:
        print("service : N/A")
    print("")
    try:
        hours = driver.find_element_by_xpath("//div[@role='button' and @jsaction='ytNONe']")
        print("hours : "+hours.text)
    except:
        print("hours : N/A")
    print("")
    try:
        contact = driver.find_element_by_xpath("//a[@data-dtype='d3ifr' and @href='#']")
        print("contact :" + contact.text)
    except:
        print("contact : N/A")
    print("")
    print("")
    print("")

