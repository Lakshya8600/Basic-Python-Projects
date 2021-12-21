from tkinter import *

#creates screen
console = Tk()

#size of screen : syntax("num1xnum2")
console.geometry("500x500")

# minimun size of screen : syntax (num1,num2)
console.minsize(100,100)
console.maxsize(600,600)

# used to label (user cannot change this)
line = Label(text="hello everyone")
# this is necessory
line.pack()

#declaring image
photo = PhotoImage(file="minecraft #1.png")
#presenting it
pic = Label(image=photo)
pic.pack()

#add title
console.title("hello")

# Important Label Options
# text - adds the text
# bd - background
# fg - foreground
# font - sets the font
# 1. font=("comicsansms", 19, "bold")
# 2. font="comicsansms 19 bold"
# padx - x padding
# pady - y padding
# relief - border styling - SUNKEN, RAISED, GROOVE, RIDGE


# Important Pack options
# anchor = nw
# side = top, bottom, left, right
# fill
# padx
# pady

# title_label.pack(side=BOTTOM, anchor ="sw", fill=X)
# title_label.pack(side=LEFT, fill=Y, padx=34, pady=34)


# present screen
console.mainloop()