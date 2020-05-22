# This is just testing if using random decision can bypass instagram's block. 
# Spoiler alert, it can't! Still got blocked.
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
import pyautogui
from selenium.webdriver.common.keys import Keys
import random


driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get('http://instagram.com')
driver.find_element_by_name('username').send_keys('-')
driver.find_element_by_name('password').send_keys('-' + Keys.RETURN)
commentList = ['Really nice!','Great!','Absolutely love it :)',
'Love it so muchhh!','WOOOOOW! amazing !!!','Just AMAZAING!!!']

pyautogui.press('right')
sleep(5)
for i in range(20):
    dice = random.choice(['like','comment','comment','next'])
    
    if dice == 'like':
        sleep(2)
        driver.find_elements_by_class_name('wpO6b')[0].click()
        sleep(0.5)
        print('liked')
        pyautogui.press('right')
        
    elif dice == 'comment':
        sleep(2)
        comment = random.choice(commentList)
        driver.find_elements_by_class_name('wpO6b')[1].click()
        driver.find_element_by_tag_name('textarea').send_keys(comment + Keys.RETURN)
        sleep(1)
        print(comment)
        pyautogui.press('right')
        
    else:
        sleep(2)
        print('skipped')
        pyautogui.press('right')
        
