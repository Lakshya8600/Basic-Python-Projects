import pyautogui  # pip install pyautogui
from PIL import Image, ImageGrab  # pip install pillow
# from numpy import asarray
import time


def hit(key):
    pyautogui.keyDown(key)
    return


def isCollide(data):
    # Draw the rectangle for birds
    # for i in range(300, 415):
    #     for j in range(410, 563):
    #         if data[i, j] < 100:
    #             hit("down")
    #             return

    for i in range(490, 500):
        for j in range(270, 305):
            if data[i, j] < 100:
                hit("up")
                return
    return


if __name__ == "__main__":
    time.sleep(1)
    hit("up")
    while True:
        image = ImageGrab.grab().convert('L')
        data = image.load()
        isCollide(data)


        # for i in range(480, 490):
        #     for j in range(270, 305):
        #         data[i, j] = 100
        
        # image.show()
        # break

