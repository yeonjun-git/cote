import time 
import pyautogui 

## for test

cnt = 0

while True:
    
    pyautogui.moveTo(100,100)
    pyautogui.click()
    cnt+=1
    print("move(100,100)", cnt)    
    time.sleep(5)

    pyautogui.moveTo(500,500)
    pyautogui.click()
    cnt+=1
    print("move(600,600)", cnt)
    time.sleep(5)

    pyautogui.moveTo(1200,1200)
    pyautogui.click()
    cnt+=1
    print("move(1200,1200)", cnt)    
    time.sleep(5)

    pyautogui.moveTo(1800,1800)
    pyautogui.click()
    cnt+=1
    print("move(1800,1800)", cnt)    
    time.sleep(5)
