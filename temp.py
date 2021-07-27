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
 
'''try:
    link = WebDriverWait(driver, 40).until(
        EC.presence_of_element_located((By.PARTIAL_LINK_TEXT, "web results for "))
    )
    link.click()
    
    view_all = WebDriverWait(driver, 40).until(
        EC.presence_of_element_located((By.PARTIAL_LINK_TEXT, "View all"))
    )
    view_all.click()
    main = WebDriverWait(driver, 90).until(
        EC.presence_of_element_located((By.CLASS_NAME, "rl_tile-group"))
    )
    elements = main.find_elements_by_class_name("dbg0pd")
    for name in elements:
        name.click()
        address = WebDriverWait(driver, 30).until(
            EC.presence_of_element_located((By.CLASS_NAME, "Z1hOCe"))
        )
        rating = WebDriverWait(driver, 30).until(
            EC.presence_of_element_located((By.CLASS_NAME, "Ob2kfd"))
        )
        service = WebDriverWait(driver, 30).until(
            EC.presence_of_element_located((By.TAG_NAME, "c-wiz"))
        )
        Hours = WebDriverWait(driver, 30).until(
            EC.presence_of_element_located((By.CLASS_NAME, "TLou0b"))
        )
        contact = WebDriverWait(driver, 30).until(
            EC.presence_of_element_located((By.CLASS_NAME, "LrzXr.zdqRlf.kno-fv"))
        )
        print(name.text)
        print(contact.text)
        print(Hours.text)
        print(service.text)
        print(rating.text)
        print(address.text)
        print("")
        driver.back()
except:
    print("name is ")'''

view_all = WebDriverWait(driver, 90).until(
    EC.presence_of_element_located((By.PARTIAL_LINK_TEXT, "View all"))
)
view_all.click()
main = WebDriverWait(driver, 90).until(
    EC.presence_of_element_located((By.CLASS_NAME, "rl_tile-group"))
)
elements = main.find_elements_by_class_name("dbg0pd")
for i in elements:
    try:
        print(i.text)
    except:
        continue
    temp= main.find_element_by_partial_link_text(i.text).click()
    #temp.click()
    time.sleep(5)
    try:
        address= driver.find_element_by_class_name("Z1hOCe")
        print("address : "+address.text)
    except:
        print("address : N/A" )
    try:
        rating = driver.find_element_by_class_name("Ob2kfd")
        print("rating : "+rating.text)
    except:
        print("ratings : N/A")
    try:
        service = driver.find_element_by_tag_name("c-wiz")
        print("service : "+service.text)
    except:
        print("service : N/A")
    try:
        hours = driver.find_element_by_class_name("TLou0b")
        print("hours : "+hours.text)
    except:
        print("hours : N/A")
    try:
        contact = driver.find_element_by_class_name("LrzXr.zdqRlf.kno-fv")
        print("contact :" + contact.text)
    except:
        print("contact : N/A")

    print("")

    '''service = WebDriverWait(driver, 30).until(
        EC.presence_of_element_located((By.TAG_NAME, "c-wiz"))
    )
    Hours = WebDriverWait(driver, 30).until(
        EC.presence_of_element_located((By.CLASS_NAME, "TLou0b"))
    )
    contact = WebDriverWait(driver, 30).until(
        EC.presence_of_element_located((By.CLASS_NAME, "LrzXr.zdqRlf.kno-fv"))
    )'''

# try to find eleement by partially link name
'''
elements = main.find_elements_by_class_name("dbg0pd")
for name in elements:
    time.sleep(10)
    name.click()
    print("kkkk")
    address = WebDriverWait(driver, 30).until(
        EC.presence_of_element_located((By.CLASS_NAME, "Z1hOCe"))
    )
    rating = WebDriverWait(driver, 30).until(
        EC.presence_of_element_located((By.CLASS_NAME, "Ob2kfd"))
    )
    service = WebDriverWait(driver, 30).until(
        EC.presence_of_element_located((By.TAG_NAME, "c-wiz"))
    )
    Hours = WebDriverWait(driver, 30).until(
        EC.presence_of_element_located((By.CLASS_NAME, "TLou0b"))
    )
    contact = WebDriverWait(driver, 30).until(
        EC.presence_of_element_located((By.CLASS_NAME, "LrzXr.zdqRlf.kno-fv"))
    )
    print(name.text)
    print(contact.text)
    print(Hours.text)
    print(service.text)
    print(rating.text)
    print(address.text)
    print("")
    driver.back()'''
