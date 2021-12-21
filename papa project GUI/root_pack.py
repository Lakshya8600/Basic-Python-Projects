from tkinter import *
import datetime

root = Tk()

root_length = 1330
root_breath = 690
root_screen_width = root.winfo_screenwidth()
root_screen_height = root.winfo_screenheight()
tdate = datetime.date.today()
wdate = "enable it"
# wdate = intro.date.get()    enable it

root.geometry(f"{root_length}x{root_breath}")
root.resizable(False,False)
x_cordinate = int((root_screen_width/2) - (root_length/2))
y_cordinate = int((root_screen_height/2) - (root_breath-310))
root.geometry("{}x{}+{}+{}".format(root_length, root_breath, x_cordinate, y_cordinate))
root.configure(bg="grey")

#date window
f = Frame(root,relief=SUNKEN,borderwidth=5,bg="grey",padx=10)
Label(f,text=f"Today's Date - {tdate}",font="lucida 15 bold",bg="grey").pack(side=TOP,anchor="e")
Label(f,text=f"Working date - {wdate}",font="lucida 15 bold",bg="grey").pack(side=TOP,anchor="e")
f.pack(fill=X)

#Opening stock , CLOSING and SALE
#padx = 97
f1 = Frame(root,relief=SUNKEN,borderwidth=5,bg="white")
Label(f1,text="OPENING STOCK",bg="silver",font="lucida 20 bold",padx=97).pack()
f1.pack(side=LEFT,anchor="n",fill=X)

#padx = 140
f1 = Frame(root,relief=SUNKEN,borderwidth=5,bg="white")
Label(f1,text="PURCHASE",bg="silver",font="lucida 20 bold",padx=14).pack()
f1.pack(side=LEFT,anchor="n")

#padx = 180
f1 = Frame(root,relief=SUNKEN,borderwidth=5,bg="white")
Label(f1,text="SALE",bg="silver",font="lucida 20 bold",padx=18).pack()
f1.pack(side=LEFT,anchor="n")

# QUantity Rate Amount
f1 = Frame(root,relief=SUNKEN,borderwidth=5,bg="white")
Label(f1,text="lakshya",bg="silver",font="lucida 20 bold").pack()
f1.pack(side=LEFT,anchor="s")

root.mainloop()