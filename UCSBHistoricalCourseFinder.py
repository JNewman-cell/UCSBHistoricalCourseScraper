from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time
from datetime import date
import pandas as pd

ID = "id"
XPATH = "xpath"
NAME = "name"
CLASS_NAME = "class_name"\

# every course topic you are interested in
courses = ['Computer Science - CMPSC', 'Electrical Computer Engineering - ECE']
# list for every course topic inputted
csCourses = []
eceCourses = []
quarters = {1: 'winter', 2: 'spring', 4: 'fall'}
todays_date = date.today()

# Using Safari to access web
driver = webdriver.Chrome()
# Open the SHS website
driver.get('https://my.sa.ucsb.edu/gold/')
print('opened webpage')
driver.maximize_window()
# enter login information, then submit
driver.find_element(By.ID, 'pageContent_userNameText').send_keys(
    # username as string)
print('inputted username')
driver.find_element(By.ID, 'pageContent_passwordText').send_keys(
    # password as string)
print('inputted password')
driver.find_element(By.ID, 'pageContent_loginButton').click()
print('logged in')
for course in courses:
    # switch to the "Find Courses" Page
    driver.find_element(By.ID, 'Li1').click()
    secondlistelement=Select(driver.find_element(
        By.XPATH, '//*[@id="pageContent_subjectAreaDropDown"]'))
    # search for classes in Course "i"
    secondlistelement.select_by_visible_text(course)
    time.sleep(1)
    # for loop to loop through each quarter of topic specific courses
    for key, val in quarters.items():
        listelement=Select(driver.find_element(
            By.ID, 'pageContent_quarterDropDown'))
        # search for classes that happened in current Quarter last year
        listelement.select_by_value(str(todays_date.year-1)+str(key))
        time.sleep(1)
        driver.find_element(By.ID, 'pageContent_searchButton').click()
        # collect all the courses on the webpage into a single dictionary
        allCourses=driver.find_elements(By.CLASS_NAME, 'courseTitle')
        print('found courses')
        # if the subject is computer science, then add it to the dictionary
        if course == courses[0]:
            for c in allCourses:
                csCourses.append(c.text)
            dict={'CS '+val: csCourses}
            df=pd.DataFrame(dict)
            df.to_csv((courses[0])[courses[0].rfind(' ')+1:] +
                      val+'_classes.csv', index=False, header=True)
            csCourses.clear()
        # if the subject is computer science, then add it to the dictionary
        elif course == courses[1]:
            for c in allCourses:
                eceCourses.append(c.text)
            dict={'ECE '+val: eceCourses}
            df=pd.DataFrame(dict)
            df.to_csv((courses[1])[courses[1].rfind(' ')+1:] +
                      val+'_classes.csv', index=False, header=True)
            eceCourses.clear()
        time.sleep(5)
        driver.find_element(By.ID, 'Li1').click()


driver.quit()
