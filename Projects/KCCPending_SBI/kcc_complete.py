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


edge_options=webdriver.EdgeOptions()
# driver_path='./msedgedriver.exe'
driver = webdriver.Edge(options=edge_options)

driver.get('https://fasalrin.gov.in/')

# try:
#     with open('cookies.pkl','rb') as file:
#         cookies=pickle.load(file)
#         for cookie in cookies:
#             driver.add_cookie(cookie)

#     driver.refresh()

#     driver.get('https://fasalrin.gov.in/welcome')
# except:
#     print("Cookie not found")

df = pd.read_excel('E:\Personal_Development\Personal_Development\Projects\KCCPending_SBI\lcwe.xlsx', sheet_name='Sheet1')

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

# cookies=driver.get_cookies()
# with open('cookies.pkl','wb') as file:
#     pickle.dump(cookies,file)
# Alert Screen 
# alert_ok_button=driver.find_element(By.CLASS_NAME,'btn genBlackOutlineBtn alertBodyModalBtn')
# alert_ok_button.click()

# KCC Screen
# dashboard_button=driver.find_element(By.XPATH,f"//*[@title='Dashboard']")
# dashboard_button.click()

# WebDriverWait(driver,10).until(EC.presence_of_element_located((By.CLASS_NAME,'btn btn-btn view-details yellow-btn')))

# 


# WebDriverWait(driver,10).until(EC.presence_of_element_located((By.CLASS_NAME,'ms-sm-0 ms-auto claimBtnBox')))

# # Draft Screen
# proceed_section=driver.find_element(By.CLASS_NAME,'ms-sm-0 ms-auto claimBtnBox');
# proceed_section.find_element(By.TAG_NAME,'button').click()

# WebDriverWait(driver,10).until(EC.presence_of_element_located((By.CLASS_NAME,'loanApplicationTable')))

# total_count=driver.find_element(By.XPATH,"//*[text()='Total Count: ']")
# print(total_count.text)

no_data_accounts=[]

try:
    with open('E:\Personal_Development\Personal_Development\Projects\KCCPending_SBI\empty_acc.pkl','rb') as file:
        no_data_accounts=pickle.load(file)
except Exception as e:
    print("Error: ",e)
    no_data_accounts=[]
    

    # print("Total Rows:",len(rows))
isSuccess=True
for i in range(0,50):
    try:
        if(isSuccess):
            isSuccess=False
            try:
                WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH,"//*[text()=' View Details']")))
                driver.find_elements(By.XPATH,"//*[text()=' View Details']")[2].click()

                WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH,"//*[text()='PROCEED']")))
                driver.find_element(By.XPATH,"//*[text()='PROCEED']").click()
            except:
                print("No Proceed Button")

        WebDriverWait(driver,15).until(EC.presence_of_element_located((By.CLASS_NAME,'loanApplicationTable')))
        table_body=driver.find_element(By.TAG_NAME,'tbody')
        rows=table_body.find_elements(By.TAG_NAME,'tr')
        WebDriverWait(driver,10).until(EC.presence_of_element_located((By.TAG_NAME,'td')))
        columns=rows[i].find_elements(By.TAG_NAME,'td')
        # driver.find_element(By.NAME,'search').send_keys(columns[0].text)
        accountNo=columns[5].text
        if(accountNo in no_data_accounts):
            continue
        edit_button=columns[7].find_element(By.CLASS_NAME,'action-container').find_elements(By.TAG_NAME,'button')[0]
        edit_button.click()
        WebDriverWait(driver,10).until(EC.presence_of_element_located((By.NAME,'resStateId')))
        back_button=driver.find_element(By.XPATH,"//*[text()='BACK']")
        state_select=Select(driver.find_element(By.NAME,'resStateId'))
        if(state_select.first_selected_option.text=='Select'):
            # try:
            #     back_button.click()
            # except:
            #     if(accountNo not in no_data_accounts):
            #         no_data_accounts.append(accountNo)
            #     with open("E:\Personal_Development\Personal_Development\Projects\KCCPending_SBI\empty_acc.pkl", "wb") as file:
            #         pickle.dump(no_data_accounts, file)
            #     # time.sleep(1)
            #     back_button.click()
            # continue
            no_data_accounts.append(accountNo)
            with open("E:\Personal_Development\Personal_Development\Projects\KCCPending_SBI\empty_acc.pkl", "wb") as file:
                    pickle.dump(no_data_accounts, file)
            isSuccess=True
            driver.get('https://fasalrin.gov.in/dashboard')
            continue
        
        #Main Execution comes here
        # select agri crops
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(0.5)
        Select(driver.find_element(By.XPATH,"//*[text()='Primary Activity']/following-sibling::div").find_element(By.TAG_NAME,'select')).select_by_visible_text("Agri Crops")
        time.sleep(0.5)
        WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH,"//*[text()='UPDATE & CONTINUE']")))
        driver.find_element(By.XPATH,"//*[text()='UPDATE & CONTINUE']").click()
        # WebDriverWait(driver,10);
        # WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH,"//*[text()='UPDATE & CONTINUE']")))
        time.sleep(1.5)
        driver.find_elements(By.XPATH,"//*[text()='UPDATE & CONTINUE']")[1].click()
        
        # WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH,"//*[text()='UPDATE & CONTINUE']")))
        time.sleep(1.5)
        loanSanctionedAmount=driver.find_element(By.NAME,"loanSanctionAmount").get_attribute('value')
        driver.find_elements(By.XPATH,"//*[text()='UPDATE & CONTINUE']")[2].click()

        # print("7th column options:  ",columns[7])
        # for column in columns:
        #     print(column.text)
        print("Reading Excel Data for account",accountNo)
        excel_data=df[df["A/c No."]==int(accountNo)].loc[df[df["A/c No."]==int(accountNo)]["Total Extent"].idxmax()]
        print("Read Excel Data for Account:",accountNo)
        time.sleep(1)
        agriCorpsButton=driver.find_elements(By.XPATH,"//*[text()='Agri Crops']")
        for agri in agriCorpsButton:
            try:
                agricormbuttonclasses=agriCorpsButton.get_attribute('class')
                if(agricormbuttonclasses.find('act_tab_btn_selected')==-1):
                    agriCorpsButton.click()
            except:
                print("Button not interactable")

        WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.NAME,"cropCode")))
        Select(driver.find_element(By.NAME,"cropCode")).select_by_visible_text("Bengal Gram (Chana) - IR")
        surveyNo=str(excel_data['Survey No'])
        driver.find_element(By.NAME,"surveyNumber").send_keys(surveyNo)
        khataNo=str(excel_data['Khata No'])
        driver.find_element(By.NAME,"khataNumber").send_keys(khataNo)
        landArea=float(excel_data['Total Extent'])
        driver.find_element(By.NAME,"landArea").send_keys(landArea)
        Select(driver.find_element(By.NAME,"landType")).select_by_visible_text("IRRIGATED")
        Select(driver.find_element(By.NAME,"seasonCode")).select_by_visible_text("KHARIF")

        # Location Finding
        driver.find_element(By.CLASS_NAME,"find-loc").click()
        time.sleep(1)
        WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH,"//*[text()='Block / Subdistrict']")))
        Select(driver.find_element(By.NAME,"landDistrictID")).select_by_visible_text("Nandyal")
        time.sleep(1)
        Select(driver.find_element(By.NAME,"landSubDistrictID")).select_by_visible_text("Dhone")
        time.sleep(1)

        # village=excel_data['English Village']
        # try:
        #     Select(driver.find_element(By.NAME,"landVillageID")).select_by_visible_text(village)
        # except:
        #     input("Village name not available in the list. Press Enter to continue...")
            
        Select(driver.find_element(By.NAME,"landVillageID")).select_by_visible_text("Dhone")
        driver.find_element(By.XPATH,"//*[text()='PROCEED']").click()
        time.sleep(1)


        saveContinue=driver.find_elements(By.XPATH,"//*[text()='SAVE & CONTINUE']")
        updateContinue=driver.find_elements(By.XPATH,"//*[text()='UPDATE & CONTINUE']")
        if(len(saveContinue)>0):
            saveContinue[0].click()
            loanSctioninp=driver.find_element(By.NAME,"loanSanctionedAmount")
            loanSctioninp.clear()
            loanSctioninp.send_keys(loanSanctionedAmount)
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
        # driver.find_elements(By.XPATH,"//*[text()='BACK']")[3].click()

        # driver.find_elements(By.XPATH,"//*[text()='BACK']")[3].click()
        # isSuccess=True
        print("--------------------------------------------------")
    except(Exception) as e:
        print("Error: ",e)
        if(accountNo not in no_data_accounts):
            no_data_accounts.append(accountNo)
        with open("E:\Personal_Development\Personal_Development\Projects\KCCPending_SBI\empty_acc.pkl", "wb") as file:
            pickle.dump(no_data_accounts, file)
        isSuccess=True
        driver.get('https://fasalrin.gov.in/dashboard')

# print("Total Count:",total_count.text)

input("Press Enter to continue...")

