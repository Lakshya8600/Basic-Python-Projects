import pyautogui
import pyperclip
import time

try:
    va = int(input("Enter The Number Of Files You Want To Scan \n"))
except expression as identifier:
    Print("Pls Enter A Suitable OutPut")

time.sleep(2)
i = 0
while(i<va):
    pyautogui.press('down')
    pyautogui.press('f2')
    pyautogui.hotkey('ctrl','c')
    time.sleep(1)
    var = pyperclip.paste()
    var = var.lstrip('y2mate.com - ')
    pyautogui.write(var)
    pyautogui.press('enter')
    i+=1

