import requests
import json
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
import pickle
import time

data=pd.read_excel('E:\Personal_Development\Personal_Development\Projects\KCCPending_SBI\lclat2.xlsx',sheet_name='Sheet1')

print("Excel read")

edge_options=webdriver.EdgeOptions()
# driver_path='./msedgedriver.exe'
driver = webdriver.Edge(options=edge_options)

driver.get('https://fasalrin.gov.in/')

# Login Screen Redirection
profile_button=driver.find_element(By.XPATH,f"//*[@title='Kisan Credit Card - Login']") 
profile_button.click()

login_button=driver.find_element(By.CLASS_NAME,'login-sign');
login_button.click()

WebDriverWait(driver,10).until(EC.presence_of_element_located((By.NAME,'username')))

mobile_number_inp=driver.find_element(By.NAME,'username')
mobile_number_inp.send_keys('8500793416')

password_inp=driver.find_element(By.NAME,'loginPwd')
password_inp.send_keys('123456+S')

input("Do Captha and continue then press enter")

WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH,"//*[text()=' View Details']")))
driver.find_elements(By.XPATH,"//*[text()=' View Details']")[2].click()

WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH,"//*[text()='PROCEED']")))
driver.find_element(By.XPATH,"//*[text()='PROCEED']").click()
# WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH,"//button[contains(@class,'btn genBlackOutlineBtn alertBodyModalBtn')]")))
# driver.find_element(By.XPATH,"//button[contains(@class,'btn genBlackOutlineBtn alertBodyModalBtn')]").click()

WebDriverWait(driver,20).until(EC.presence_of_element_located((By.CLASS_NAME,"loanApplicationTable")))
searchBox=driver.find_element(By.XPATH,"//input[contains(@type,'search')]")
isSuccess=False
try:
    for i,row in data.iterrows():
        if(row[42]=='yes'):
            continue
        # try:
        if(isSuccess):
            isSuccess=False
            WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH,"//*[text()=' View Details']")))
            driver.find_elements(By.XPATH,"//*[text()=' View Details']")[2].click()

            WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH,"//*[text()='PROCEED']")))
            driver.find_element(By.XPATH,"//*[text()='PROCEED']").click()
            # WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH,"//button[contains(@class,'btn genBlackOutlineBtn alertBodyModalBtn')]")))
            # driver.find_element(By.XPATH,"//button[contains(@class,'btn genBlackOutlineBtn alertBodyModalBtn')]").click()

            WebDriverWait(driver,20).until(EC.presence_of_element_located((By.CLASS_NAME,"loanApplicationTable")))
            searchBox=driver.find_element(By.XPATH,"//input[contains(@type,'search')]")
        print(i,row)
        searchBox.clear()
        searchBox.send_keys(row[0])
        driver.find_element(By.XPATH,"//input[contains(@type,'search')]/following-sibling::button").click()
        time.sleep(0.01)
        table_body=driver.find_element(By.TAG_NAME,'tbody')
        rows=table_body.find_elements(By.TAG_NAME,'tr')
        if(rows[0].text=='No record(s) found'):
            data.at[i,'DataAdded']='yes'
            continue
        WebDriverWait(driver,10).until(EC.presence_of_element_located((By.TAG_NAME,'td')))
        columns=rows[0].find_elements(By.TAG_NAME,'td')
        accountNo=columns[5].text
        edit_button=columns[7].find_element(By.CLASS_NAME,'action-container').find_elements(By.TAG_NAME,'button')[0]
        edit_button.click()
        WebDriverWait(driver,10).until(EC.presence_of_element_located((By.NAME,'resStateId')))
        currentTab=driver.find_element(By.XPATH,"//*[contains(@class,'fade tab-pane active show')]")
        WebDriverWait(currentTab,10).until(EC.presence_of_element_located((By.XPATH,"//button[text()='UPDATE & CONTINUE']")))
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        currentTab.find_element(By.XPATH,"//button[text()='UPDATE & CONTINUE']")
        Select(driver.find_element(By.XPATH,"//*[text()='Primary Activity']/following-sibling::div").find_element(By.TAG_NAME,'select')).select_by_visible_text("Agri Crops")
        time.sleep(1)
        currentTab.find_element(By.XPATH,"//*[text()='UPDATE & CONTINUE']").click()
        # WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH,"//*text()='UPDATE & CONTINUE']")))
        currentTab=driver.find_element(By.XPATH,"//*[contains(@class,'fade tab-pane active show')]")
        WebDriverWait(currentTab,10).until(EC.presence_of_element_located((By.XPATH,"//button[text()='UPDATE & CONTINUE']")))
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

        # stateDetaisl=Select(driver.find_element(By.NAME,"resStateId"))
        # if(stateDetaisl.first_selected_option.text=="Select"):
        #     stateDetaisl.select_by_visible_text("ANDHRA PRADESH")
        #     time.sleep(1)
        #     districtDetails=Select(driver.find_element(By.NAME,"resDistrictId"))
        #     districtDetails.select_by_visible_text("Nandyal")
        #     time.sleep(1)
        #     Select(driver.find_element(By.NAME,"resSubDistrictId")).select_by_visible_text("Dhone")
        #     time.sleep(1)
        #     Select(driver.find_element(By.NAME,"resVillageId")).select_by_visible_text("Dhone")


        streetAddress=driver.find_element(By.NAME,"resAddress")
        if(len(streetAddress.get_attribute('value'))<10):
            streetAddress.send_keys(" Street Address")
        # WebDriverWait(currentTab,10).until(EC.element_to_be_clickable((By.XPATH,"//button[text()='UPDATE & CONTINUE']")))
        driver.execute_script("arguments[0].click();",currentTab.find_element(By.XPATH,"//button[text()='UPDATE & CONTINUE']"))
        time.sleep(1)
        currentTab.find_elements(By.XPATH,"//button[text()='UPDATE & CONTINUE']")[1].click()
        currentTab=driver.find_element(By.XPATH,"//*[contains(@class,'fade tab-pane active show')]")
        WebDriverWait(currentTab,10).until(EC.presence_of_element_located((By.XPATH,"//button[text()='UPDATE & CONTINUE']")))
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        loanSanctionedAmount=driver.find_element(By.NAME,"loanSanctionAmount").get_attribute('value')
        time.sleep(1)
        currentTab.find_elements(By.XPATH,"//button[text()='UPDATE & CONTINUE']")[2].click()
        currentTab=driver.find_element(By.XPATH,"//*[contains(@class,'fade tab-pane active show')]")
        WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH,"//button[text()='Agri Crops']")))
        time.sleep(1)
        agriCropBtn=driver.find_element(By.XPATH,"//button[text()='Agri Crops']")
        cropData=driver.find_elements(By.ID,"cropHusbandry");
        if len(cropData)==0:
            agriCropBtn.click()
            WebDriverWait(driver,10).until(EC.presence_of_element_located((By.ID,"cropHusbandry")))
        cropData=driver.find_elements(By.ID,"cropHusbandry");
        WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.NAME,"cropCode")))
        Select(driver.find_element(By.NAME,"cropCode")).select_by_visible_text("Bengal Gram (Chana) - IR")
        driver.find_element(By.NAME,"surveyNumber").send_keys(str(row[2]))
        driver.find_element(By.NAME,"khataNumber").send_keys(str(row[3]))
        driver.find_element(By.NAME,"landArea").send_keys(float(row[4]))
        Select(driver.find_element(By.NAME,"landType")).select_by_visible_text("IRRIGATED")
        Select(driver.find_element(By.NAME,"seasonCode")).select_by_visible_text("KHARIF")
        driver.find_element(By.CLASS_NAME,"find-loc").click()

        WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.NAME,"landDistrictID")))
        time.sleep(1)
        Select(driver.find_element(By.NAME,"landDistrictID")).select_by_visible_text("Nandyal")
        time.sleep(1)
        Select(driver.find_element(By.NAME,"landSubDistrictID")).select_by_visible_text("Dhone")
        time.sleep(1)
        Select(driver.find_element(By.NAME,"landVillageID")).select_by_visible_text("Dhone")
        driver.find_element(By.XPATH,"//*[text()='PROCEED']").click()
        # WebDriverWait(currentTab,10).until(EC.element_to_be_clickable((By.XPATH,"//*[text()='UPDATE & CONTINUE']")))
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(1)
        # currentTab.find_elements(By.XPATH,"//*[text()='UPDATE & CONTINUE']")[3].click()
        saveContinue=driver.find_elements(By.XPATH,"//*[text()='SAVE & CONTINUE']")
        updateContinue=driver.find_elements(By.XPATH,"//*[text()='UPDATE & CONTINUE']")
        if(len(saveContinue)>0):
            saveContinue[0].click()
            loanSctioninp=driver.find_element(By.NAME,"loanSanctionedAmount")
            loanSctioninp.clear()
            loanSctioninp.send_keys(loanSanctionedAmount)
            saveContinue[0].click()
        elif(len(updateContinue)>0):
            updateContinue[3].click()
        time.sleep(1)
        WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH,"//*[text()='Preview']")))
        driver.find_element(By.XPATH,"//*[text()='Preview']").click()

        try:
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(1)
            driver.find_element(By.XPATH,"//*[text()='SUBMIT']").click()
        except:
            time.sleep(1)
            driver.find_element(By.XPATH,"//*[text()='SUBMIT']").click()
        WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH,"//*[text()='CONFIRM']")))
        time.sleep(1)
        driver.find_element(By.XPATH,"//*[text()='CONFIRM']").click()

        WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH,"//*[text()='OK']")))
        time.sleep(1)
        driver.find_element(By.XPATH,"//*[text()='OK']").click()

        # WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH,"//*[text()='BACK']")))
        time.sleep(1)
        isSuccess=True
        driver.get('https://fasalrin.gov.in/dashboard')
        print("Completed:",i)
        print("....................----------------------------------....................")
        data.at[i,'DataAdded']='yes'
        # except Exception as e:
        #     print(e)
        #     isSuccess=True
        #     driver.get('https://fasalrin.gov.in/dashboard')
        #     continue
except Exception as e:
    print("Exception:",e)
    data.to_excel('E:\Personal_Development\Personal_Development\Projects\KCCPending_SBI\lclat2.xlsx',sheet_name='Sheet1',index=False)
    raise e