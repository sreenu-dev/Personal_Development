from operator import contains
import time
from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


service=Service("E:/Personal_Development/Personal_Development/Projects/Percipio_Auto_Complete/edgedriver_win64/msedgedriver.exe")
driver=webdriver.Edge(service=service)

print(driver.title)

driver.get("https://wd103.myworkday.com/accenture/learning/course/c2b4d4851b3610016ca0d40d91ae0000/lesson/bd05a1f5c5d01001fb5282ade33e0002?record=6d0e5a94ad241001774359d2d1280000&type=9882927d138b100019b928e75843018d")

Questions_data=[]

input("Press to start debug")

# lauch_button=driver.find_element(By.XPATH,"//button[contains(@class,'e1medudu0 css-1mttr8q')]")
# lauch_button.click()

# main_window_handle=driver.current_window_handle

# # Wait for the new window to open
# WebDriverWait(driver, 20).until(lambda d: len(d.window_handles) > 1)

# window_handles=driver.window_handles

# for window in window_handles:
#     if(window!=main_window_handle):
#         driver.switch_to.window(window)
#         break

def checkCorrectAns(op):
    paths=op.find_elements(By.TAG_NAME,"path")
    if(len(paths)>0):
        for p in paths:
            if(p.get_attribute('fill')=='#275114'):
                return True
        return False
    else:
        return False
print("Mini window title",driver.title)

driver.switch_to.window(driver.window_handles[1])

def checkAnsAndDoQuestions():
    WebDriverWait(driver,40).until(
        EC.presence_of_element_located((By.XPATH,"//div[contains(@class,'slide-object slide-object-vectorshape shown')]"))
    )
    question=""
    current_question=None
    try:
        for i in range(0,47):
            current_question=None
            WebDriverWait(driver,40).until(
                EC.presence_of_element_located((By.XPATH,"//div[contains(@class,'slide-object slide-object-vectorshape shown')]"))
            )
            items=driver.find_elements(By.XPATH,"//div[contains(@class,'slide-object slide-object-vectorshape shown')]")
            # for i in items:
                # text_inside=i.get_attribute("data-acc-text")
                # if("Question" in text_inside):
                #     console.log("QUestion Number:",int(text_inside.split(" ")[1]))
                #     if(int(text_inside.split(" ")[1])==1):
                #         question=driver.find_elements(By.XPATH,"//div[contains(@class,'slide-object slide-object-vectorshape shown')]")[-5].get_attribute("data-acc-text")
                #     else:
                #         question=driver.find_elements(By.XPATH,"//div[contains(@class,'slide-object slide-object-vectorshape shown')]")[-6].get_attribute("data-acc-text")
            if(i==0):
                question=driver.find_elements(By.XPATH,"//div[contains(@class,'slide-object slide-object-vectorshape shown')]")[-5].get_attribute("data-acc-text")
                next_button=driver.find_elements(By.XPATH,"//div[contains(@class,'slide-object slide-object-vectorshape shown')]")[-2]
            else:
                question=driver.find_elements(By.XPATH,"//div[contains(@class,'slide-object slide-object-vectorshape shown')]")[-6].get_attribute("data-acc-text")
                next_button=driver.find_elements(By.XPATH,"//div[contains(@class,'slide-object slide-object-vectorshape shown')]")[-3]

            if(len(Questions_data)==0):
                question_details={'question':question,'options':[],'ans':[]}
                current_question=question_details
                Questions_data.append(question_details)
            else:
                for q in Questions_data:
                    if(q['question']==question):
                        current_question=q
                        break
                if(current_question==None):
                    question_details={'question':question,'options':[],'ans':[]}
                    current_question=question_details
                    Questions_data.append(question_details)
            options_elem = driver.find_elements(By.XPATH,"//div[contains(@class,'slide-object slide-object-vectorshape shown cursor-default')]")
            for op in options_elem:
                current_question['options'].append(op.get_attribute("data-acc-text"))
                isCorrectAns=checkCorrectAns(op)
                if(isCorrectAns):
                    current_question['ans'].append(op.get_attribute("data-acc-text"))
            
            next_button.click()
            time.sleep(1)
    except Exception as e:
        print("Error",e)
        print("Questions_data",Questions_data)
        print("Current Question",current_question)


    print("Working")

    print("Questions Data")
    print(Questions_data)
    input("Question Data Completed")

    WebDriverWait(driver,40).until(
        EC.presence_of_element_located((By.XPATH,"//div[contains(@class,'slide-object slide-object-vectorshape shown cursor-hover')]"))
    )
    main_buttons=driver.find_elements(By.XPATH,"//div[contains(@class,'slide-object slide-object-vectorshape shown cursor-hover')]")
    main_buttons[0].click()

    correctAnsCount=0
    try:
        for i in range(0,47):
            WebDriverWait(driver,40).until(
                EC.presence_of_element_located((By.XPATH,"//div[contains(@class,'slide-object slide-object-vectorshape shown cursor-hover')]"))
            )
            items=driver.find_elements(By.XPATH,"//div[contains(@class,'slide-object slide-object-vectorshape shown')]")
            if(i==0):
                question=driver.find_elements(By.XPATH,"//div[contains(@class,'slide-object slide-object-vectorshape shown')]")[-4].get_attribute("data-acc-text")
                next_button=driver.find_elements(By.XPATH,"//div[contains(@class,'slide-object slide-object-vectorshape shown')]")[-1]
            else:
                question=driver.find_elements(By.XPATH,"//div[contains(@class,'slide-object slide-object-vectorshape shown')]")[-5].get_attribute("data-acc-text")
                next_button=driver.find_elements(By.XPATH,"//div[contains(@class,'slide-object slide-object-vectorshape shown')]")[-2]
                if(i==46):
                    next_button=driver.find_elements(By.XPATH,"//div[contains(@class,'slide-object slide-object-vectorshape shown')]")[-1]
            options_data_unfiltered=driver.find_elements(By.XPATH,"//div[contains(@class,'slide-object slide-object-vectorshape shown cursor-hover')]")
            options_data=[]
            for o in options_data_unfiltered:
                if(o.get_attribute("data-acc-text")!='Next'):
                    options_data.append(o)
            found_ans=False
            for q in Questions_data:
                if(q['question']==question):
                    correctAnsCount+=1
                    for a in q['ans']:
                        for op in options_data:
                            if(op.get_attribute("data-acc-text")==a):
                                op.click()
                                found_ans=True
                    break
            if found_ans==False:
                options_data[0].click()

            next_button.click()
            time.sleep(1)
    except Exception as e:
        print("Error",e)
    print("Correct Ans Count",correctAnsCount)
    decision_input=input("Would you like to do one more iteration? (Y/N)")
    if(decision_input=="Y" or decision_input=="y"):
        checkAnsAndDoQuestions()


oneVale="Working"

checkAnsAndDoQuestions()

input("Press Enter to close the browser")
driver.quit()


q="What is the foundational model we are using in GenWizard platform for application development use cases?"