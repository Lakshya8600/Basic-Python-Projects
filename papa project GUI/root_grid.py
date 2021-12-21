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
f = Frame(root,relief=SUNKEN,borderwidth=0,bg="grey",padx=10)
Label(f,text=f"Today's Date - {tdate}",font="lucida 15 bold",bg="grey").pack(side=TOP,anchor="e",fill=X)
Label(f,text=f"Working date - {wdate}",font="lucida 15 bold",bg="grey").pack(side=TOP,anchor="e",fill=X)
f.grid(row=0,column=1,stick="nsew")

#Opening stock , CLOSING and SALE
f1 = Frame(root,relief=SUNKEN,borderwidth=5,bg="white")
Label(f1,text="OPENING STOCK",bg="silver",font="lucida 20 bold",padx=97).pack()
f1.grid(row=1,column=0)

f1 = Frame(root,relief=SUNKEN,borderwidth=5,bg="white")
Label(f1,text="PURCHASE",bg="silver",font="lucida 20 bold",padx=140).pack()
f1.grid(row=1,column=1)

f1 = Frame(root,relief=SUNKEN,borderwidth=5,bg="white")
Label(f1,text="SALE",bg="silver",font="lucida 20 bold",padx=180).pack()
f1.grid(row=1,column=2)

f = Frame(root,relief=SUNKEN,borderwidth=5,bg="white")
Label(f,text="SALE",bg="silver",font="lucida 20 bold",padx=180).pack()
f.grid(row=2,column=0)

f = Frame(root,relief=SUNKEN,borderwidth=5,bg="white")
Label(f,text="SALE",bg="silver",font="lucida 20 bold",padx=180).pack()
f.grid(row=2,column=1)


# QUantity Rate Amount

root.mainloop()