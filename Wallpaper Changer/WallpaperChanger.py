import ctypes
import random
import os
from tkinter import messagebox


def ChangeWallpaper(WallpaperPath):
    ctypes.windll.user32.SystemParametersInfoW(20, 0, WallpaperPath, 0)

CurrentDir = os.getcwd()

if "Wallpaper" in os.listdir(CurrentDir):
    wallpaperList = os.listdir(CurrentDir + "\Wallpaper")

else:
    messagebox.showerror(title="Error", message="The Folder Named Wallpaper Doesn't Exists\n. PLease Make a Folder Named Wallpaper And Put Your Wallpapers in It on Location\n"+CurrentDir,)

wallpaperList = os.listdir(CurrentDir+"\Wallpaper")
FileQuantity = len(wallpaperList)
ran = random.randint(0,FileQuantity-1)
WallpaperName = wallpaperList[ran]
# print(WallpaperName)
# print(FileQuantity)
# print(wallpaperList[FileQuantity])
path = CurrentDir+"\Wallpaper\\"+WallpaperName
ChangeWallpaper(path)
# print(CurrentDir)

