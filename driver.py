from concurrent.futures import thread
import imp
from selenium import webdriver
import time
from selenium.webdriver.support.ui import Select 
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
# code for open up google form
web = webdriver.Chrome()
web.get('https://docs.google.com/forms/d/e/1FAIpQLSc9n4VVmsH21pVZbdAm8hnLB96wSpvviUrCxq5qt91J8St4xw/viewform')
time.sleep(1)
#for adding name in fields
YourName = "Heet Raval"

name = web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')

name.send_keys(YourName)

Qualification = web.find_element_by_xpath("//span[contains(text(),'Choose')]")
Qualification.click()
time.sleep(5)
web.find_element_by_xpath("(//span[contains(text(),'Post Graduation')])[2]").click()


#gender

Gender = web.find_element_by_xpath("//div//span[contains(text(),'Female')]")
Gender.click()

#interests
Interests = web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[4]/div/div/div[2]/div[1]/div[1]')
Interests.click()





#date

Date = "10-04-2022"
date = web.find_element_by_xpath("(//input[@class='whsOnd zHQkBf'])[2]")
date.send_keys(Date)


#submit
Submit = web.find_element_by_xpath("//span[contains(text(),'Submit')]")
Submit.click()