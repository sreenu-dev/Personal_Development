import time
from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

service=Service("E:/Personal_Development/Personal_Development/Projects/Percipio_Auto_Complete/edgedriver_win64/msedgedriver.exe")
driver=webdriver.Edge(service=service)

print(driver.title)

driver.get("https://accenture.percipio.com/courses/c7f2d98c-e667-43cc-a4e9-2d238237c5e5/videos/be94fb45-594b-480d-9cbd-e7a71a68bac3")

# WebDriverWait(driver, 60).until(
#     EC.presence_of_element_located((By.ID, "AccentureExchange"))
# )

# input("press to start")
# accenture_Employee=driver.find_element(By.ID, "AccentureExchange")
# accenture_Employee.click()
boti=[]

print(driver.title)

input("Press Enter to start automation")