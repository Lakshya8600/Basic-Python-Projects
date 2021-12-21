import pyautogui as pag
import time

prog_start = 2
opening_time = 15
i = 0

def message():
    time.sleep(prog_start)

    pag.click(10, 730)

    for bt in lst:
        pag.keyDown(bt)

    pag.keyDown('enter')

    time.sleep(opening_time)
    pag.click(70, 120)

    for bt in name:
        pag.keyDown(bt)

    pag.keyDown('enter')

    time.sleep(2)

    pag.click(800, 680)

    # msg = ['h','e','l','l','o']

    for b in msg:
        pag.keyDown(b)

    pag.click(1335, 690)

if __name__ == '__main__':
    lst = ['w', 'h', 'a', 't', 's', 'a', 'p', 'p']
    name = []
    msg = []

    nm = input("enter the name of person you want to sent the message\n")

    while i < len(nm):
        name.append(nm[i])
        i += 1

    # print(name)

    mg = input("enter the message you want to sent\n")

    i = 0

    while i < len(mg):
        msg.append(mg[i])
        i += 1

    message()