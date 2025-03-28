import time
from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

service=Service("E:/Personal_Development/Personal_Development/Projects/Percipio_Auto_Complete/edgedriver_win64/msedgedriver.exe")
driver=webdriver.Edge(service=service)

print(driver.title)

driver.get("https://accenture.percipio.com/courses/193bdd21-b805-40ec-99a3-6b814b8dbfca/videos/da1f9184-f706-432a-9876-9fada5c9c35c")

# WebDriverWait(driver, 60).until(
#     EC.presence_of_element_located((By.ID, "AccentureExchange"))
# )

# input("press to start")
# accenture_Employee=driver.find_element(By.ID, "AccentureExchange")
# accenture_Employee.click()
boti=[]

print(driver.title)

input("Press Enter to start automation")

def clickFinishButton():
    finishButton=driver.find_elements(By.XPATH,"//div[contains(@class,'Question---finishButton---K3V_T')]")
    if(finishButton):
        finishButton=finishButton[0]
        finishButton.click()
        time.sleep(2)
        return True

def doAutomationPercipio():
    WebDriverWait(driver, 30).until(
        EC.presence_of_element_located((By.CLASS_NAME,"PracticeQuestion---subtitle---Gnvrn"))
    )
    questions_number=driver.find_elements(By.CLASS_NAME,"PracticeQuestion---subtitle---Gnvrn")
    number_of_questions=int(questions_number[0].text.split(" ")[-1])

    print(f"Number of questions: {number_of_questions}")

    for i in range(number_of_questions):
        try:
            WebDriverWait(driver, 30).until(
                EC.presence_of_element_located((By.CLASS_NAME,"QuestionMessages---stem---2uUKi"))
            )
            question_parent=driver.find_element(By.CLASS_NAME,"QuestionMessages---stem---2uUKi")
            question=question_parent.find_element(By.TAG_NAME,"p")

            print(f"Question {i+1}: {question.text}")
            current_item=None
            if(len(boti)==0):
                item={"question":question.text,"options":[],"correctAns":[]}
                boti.append(item)
                current_item=item
            else:
                for item in boti:
                    if(item["question"]==question.text):
                        current_item=item
                        break
                if(current_item==None):
                    item={"question":question.text,"options":[],"correctAns":[]}
                    boti.append(item)
                    current_item=item
            # boti[i].question=question
            haveMultipleChoiceQuestions=driver.find_elements(By.CLASS_NAME,"MultipleChoice---choices---3APyy")
            if(haveMultipleChoiceQuestions):
                haveMultipleChoiceQuestions=haveMultipleChoiceQuestions[0]
                isMultiChoice=haveMultipleChoiceQuestions.find_elements(By.XPATH,"//input[contains(@class,'Checkbox---input---e73Wy Checkbox---labelledInputCheckbox---2oIZ5')]")
                if(isMultiChoice):
                    if(len(current_item['options'])==0):
                        options=haveMultipleChoiceQuestions.find_elements(By.CLASS_NAME,"Question---optionLabel---3Q5MS")
                        Options_list=[]
                        for option in options:
                            Options_list.append(option.text)
                        current_item['options']=Options_list   
                    if(current_item['correctAns']):
                        for ans in current_item['correctAns']:
                            # ans_elem=driver.find_element(By.XPATH,f"//div[contains(@class,'Question---optionLabel---3Q5MS') and text()=\"{ans}\"]")
                            ans_elem=driver.find_element(By.XPATH,f"//div[contains(@class,'Question---optionLabel---3Q5MS') and contains(text(),\"{ans}\")]")
                            ans_elem.click()
                    else:
                        for option in current_item['options']:
                            # option_elem=driver.find_element(By.XPATH,f"//div[contains(@class,'Question---optionLabel---3Q5MS') and text()=\"{option}\"]")
                            option_elem=driver.find_element(By.XPATH,f"//div[contains(@class,'Question---optionLabel---3Q5MS') and contains(text(),\"{option}\")]")
                            option_elem.click()
                    
                    submit_button=driver.find_element(By.XPATH,"//button[contains(@class,'Button---root---2BQqW Button---primary---1O3lq Button---small---3PMLN Button---center---13Oaw')]")
                    submit_button.click()

                    WebDriverWait(driver, 30).until(
                        EC.presence_of_element_located((By.XPATH,"//div[contains(@class,'ValidationMark---checkAnswer---1WzmX ValidationMark---visible---1m7zt')]"))
                    )
                    if(len(current_item['correctAns'])==0):
                        correct_answer_ticks=driver.find_elements(By.XPATH,"//span[contains(@class,'Icon---root---1gdAA ValidationMark---mark---5WW7u ValidationMark---colored---2rFDG ValidationMark---correct---1kz8N')]")
                        for ans_tick in correct_answer_ticks:
                            correct_ans_text=ans_tick.find_element(By.XPATH,"../../..").find_element(By.CLASS_NAME,"Question---optionLabel---3Q5MS").text
                            current_item['correctAns'].append(correct_ans_text)
                    
                    next_button=driver.find_elements(By.XPATH,"//div[contains(@class,'Question---nextButton---kq5mF')]")
                    if(next_button):
                        next_button=next_button[0]
                        next_button.click()
                    else:
                        clickFinishButton()
                    time.sleep(2)
                    continue
                isSingleChoice=driver.find_elements(By.CLASS_NAME,"RadioButton---input---3iHUk")
                if(isSingleChoice):
                    if(len(current_item['options'])==0):
                        options=haveMultipleChoiceQuestions.find_elements(By.CLASS_NAME,"Question---optionLabel---3Q5MS")
                        Options_list=[]
                        for option in options:
                            Options_list.append(option.text)
                        current_item['options']=Options_list
                    if(len(current_item['correctAns'])!=0):
                        for ans in current_item['correctAns']:
                            # ans_elem=driver.find_element(By.XPATH,f"//div[contains(@class,'Question---optionLabel---3Q5MS') and text()=\"{ans}\"]")
                            ans_elem=driver.find_element(By.XPATH,f"//div[contains(@class,'Question---optionLabel---3Q5MS') and contains(text(),\"{ans}\")]")
                            ans_elem.click()
                    else:
                        for option in current_item['options']:
                            # option_elem=driver.find_element(By.XPATH,f"//div[contains(@class,'Question---optionLabel---3Q5MS') and text()=\"{option}\"]")
                            option_elem=driver.find_element(By.XPATH,f"//div[contains(@class,'Question---optionLabel---3Q5MS') and contains(text(),\"{option}\")]")
                            option_elem.click() 
                    submit_button=driver.find_element(By.XPATH,"//button[contains(@class,'Button---root---2BQqW Button---primary---1O3lq Button---small---3PMLN Button---center---13Oaw')]")
                    submit_button.click()

                    WebDriverWait(driver, 30).until(
                        EC.presence_of_element_located((By.XPATH,"//div[contains(@class,'ValidationMark---screenReaderText---S1nif')]"))
                    )
                    correct_answer_ticks=driver.find_elements(By.XPATH,"//div[contains(@class,'ValidationMark---checkAnswer---1WzmX ValidationMark---visible---1m7zt ValidationMark---correct---1kz8N')]")
                    for ans_tick in correct_answer_ticks:
                        correct_ans_text=ans_tick.find_element(By.XPATH,"..").find_element(By.CLASS_NAME,"Question---optionLabel---3Q5MS").text
                        current_item['correctAns'].append(correct_ans_text)
                    
                    next_button=driver.find_elements(By.XPATH,"//div[contains(@class,'Question---nextButton---kq5mF')]")
                    if(next_button):
                        next_button=next_button[0]
                        next_button.click()
                    else:
                        clickFinishButton()
            haveMatchingQuestions=driver.find_elements(By.CLASS_NAME,"Matching---root---3Q0Ec")
            if(haveMatchingQuestions):

                incorrect_ans_text="Incorrect answer. C is the correct answer."

                matchingRootParent=driver.find_element(By.XPATH,"//div[contains(@class,'Matching---root---3Q0Ec')]")
                
                if(True):
                    options_q=matchingRootParent.find_elements(By.XPATH,"//legend[contains(@class,'Matching---choiceTitle---3ENuZ')]")
                    for options_data in options_q:
                        option_question=options_data.text
                        current_item['options'].append(option_question)
                if(True):
                    ans_choices_data=matchingRootParent.find_elements(By.XPATH,"//li[contains(@class,'Matching---option---1L906')]")
                    for ans_data in ans_choices_data:
                        # ans_value=ans_data.find_element(By.XPATH,"//span[contains(@class,'Matching---optionLetter---1Ai3w')]").text
                        ans_text=ans_data.text
                        current_item['ans_choices'].append(ans_text)
                
                print("Not yet implemented")
                correct_ans_class="ValidationMark---checkAnswer---1WzmX ValidationMark---visible---1m7zt ValidationMark---colored---2rFDG ValidationMark---correct---1kz8N"
                input("Press Enter to continue")
        except Exception as e:
            print(f"Error occured: {e}")
            input("Error while running this")

    WebDriverWait(driver, 60).until(
        EC.presence_of_element_located((By.XPATH,"//div[contains(@class,'AnimatedCircularProgressBar---animatedDiv---L55RX')]"))
    )

    percentage_value=int(driver.find_element(By.XPATH,"//div[contains(@class,'AnimatedCircularProgressBar---animatedDiv---L55RX')]").text.split("%")[0])
    if(percentage_value<80):
        retake_button=driver.find_element(By.XPATH,"//button[contains(@class,'Button---root---2BQqW Button---primary---1O3lq Button---medium---1CC5_ Button---center---13Oaw')]")
        retake_button.click()
        doAutomationPercipio()
    else:
        print("Successfully completed the course")
        print(boti)
        # return boti

doAutomationPercipio()

# print(boti)
input("Press Enter to close the browser")
driver.quit()