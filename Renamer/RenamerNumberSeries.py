import pyautogui
import pyperclip
import time

try:
    va = int(input("Enter The Number Of Files You Want To Rename \n"))
except exception as identifier:
    print("Pls Enter A Suitable OutPut")

time.sleep(2)
i = 0
pyautogui.press('f2')
pyautogui.write(str(i))
pyautogui.press('enter')
while(i<va):
    pyautogui.press('down')
    pyautogui.press('f2')
    time.sleep(0.22)
    pyautogui.write(str(i+1))
    pyautogui.press('enter')
    i+=1
