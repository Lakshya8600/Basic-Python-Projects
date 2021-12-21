from tkinter import *
from PIL import Image, ImageTk
import tkinter.messagebox as msg

def rootwindow():
    if date.get() == "DD-MM-YYYY":
        msg.askretrycancel("ERROR","Please Enter a Valid Date")

    else:
        intro.destroy()
        return 1

intro = Tk()

#variables
window_length = 800
window_breath = 400
screen_width = intro.winfo_screenwidth()
screen_height = intro.winfo_screenheight()
date = StringVar()
datecolour = "silver"
entrycolour = "silver"
continuecolour = "silver"
background = "grey"

# Screen Size
intro.geometry(f"{window_length}x{window_breath}")
intro.resizable(False,False)
x_cordinate = int((screen_width/2) - (window_length/2))
y_cordinate = int((screen_height/2) - (window_breath/2))
intro.geometry("{}x{}+{}+{}".format(window_length, window_breath, x_cordinate, y_cordinate))
intro.configure(bg=background)

# inserting photo
photo = Image.open("photo.jpg")
pic = ImageTk.PhotoImage(image=photo)
Label(intro,image=pic).pack()

# frame
f = Frame(intro,relief=SUNKEN,borderwidth=3,bg="azure")
f1 = Frame(intro,relief=SUNKEN,borderwidth=3,bg="azure")
f2 = Frame(intro,relief=SUNKEN,borderwidth=3,bg="azure")

#Button
b = Button(f, text="CONTINUE",bg=continuecolour,command=rootwindow,font="algerian 30 bold",)
b.pack()
f.pack(side=RIGHT,anchor="s",padx=30,pady=30)

# label
Label(f1,text="DATE",font="ALGERIAN 30 bold",bg=datecolour).pack()
f1.pack(side=LEFT,anchor="n",padx=30,pady=30)

# Entry
date.set("DD-MM-YYYY")
e = Entry(f2,textvariable=date,font="lucida 30",bg=entrycolour)
e.pack()
f2.pack(side=LEFT,anchor="n",pady=30)

intro.mainloop()


