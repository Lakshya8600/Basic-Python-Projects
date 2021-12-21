from tkinter import *
from tkinter import ttk
import datetime
import pyautogui as pag



#functoins
def lk1(event):
    pag.click(399,220)


def lk2(event):
    pag.click(532, 220)

def lk3(event):
    pag.click(665,220)

def lk4(event):
    pag.click(798,220)


def lk5(event):
    pag.click(931,220)


def lk6(event):
    pag.click(1064,220)


def lk7(event):
    pag.click(1197,220)


def lk8(event):
    pag.click(1300,220)
    a = opq.get()
    b = opr.get()
    opa = a * b
    c = puq.get()
    d = pur.get()
    pua = c*d
    e = sq.get()
    f = sr.get()
    sa = e*f
    csq.set(a+c-e)
    csr.set(b+d-f)

def lk9(event):
    pag.click(133,220)


root = Tk()

root_length = 1330
root_breath = 690
root_screen_width = root.winfo_screenwidth()
root_screen_height = root.winfo_screenheight()
tdate = datetime.date.today()
wdate = "enable it"
# wdate = intro.date.get()    enable it

#screen designing
root.geometry(f"{root_length}x{root_breath}")
root.resizable(False,True)
x_cordinate = int((root_screen_width/2) - (root_length/2))
y_cordinate = int((root_screen_height/2) - (root_breath-310))
root.geometry("{}x{}+{}+{}".format(root_length, root_breath, x_cordinate, y_cordinate))
root.configure(bg="grey")

main_frame = Frame(root,bg="grey")
main_frame.pack(side = BOTTOM,fill=BOTH)

my_canvas = Canvas(main_frame,height=522,bg="grey")
my_canvas.pack(side=LEFT, fill=BOTH, expand=1)

my_scrollbar = ttk.Scrollbar(main_frame, orient=VERTICAL, command=my_canvas.yview)
my_scrollbar.pack(side=RIGHT, fill=Y)

my_canvas.configure(yscrollcommand=my_scrollbar.set)
my_canvas.bind('<Configure>', lambda e: my_canvas.configure(scrollregion = my_canvas.bbox("all")))

second_frame = Frame(my_canvas)

my_canvas.create_window((0,0), window=second_frame, anchor="nw")

#date window
f = Frame(root,relief=SUNKEN,borderwidth=3,bg="grey",padx=535)
Label(f,text=f"Today's Date - {tdate}",font="lucida 15 bold",bg="grey").pack(side=TOP,anchor="e",fill=X)
Label(f,text=f"Working date - {wdate}",font="lucida 15 bold",bg="grey").pack(side=TOP,anchor="e",fill=X)
f.place(x=0 ,y=0)

#Opening stock , CLOSING and SALE
f1 = Frame(root,relief=SUNKEN,borderwidth=5,bg="white")
Label(f1,text="PRODUCT",bg="silver",font="lucida 20 bold",padx=74,pady=24).pack()
f1.place(x=0 ,y=65)

f1 = Frame(root,relief=SUNKEN,borderwidth=5,bg="white")
Label(f1,text="OPENING STOCK",bg="silver",font="lucida 20 bold",padx=6).pack()
f1.place(x=302 ,y=65)

f1 = Frame(root,relief=SUNKEN,borderwidth=5,bg="white")
Label(f1,text="PURCHASE",bg="silver",font="lucida 20 bold",padx=39).pack()
f1.place(x=561 ,y=65)

f1 = Frame(root,relief=SUNKEN,borderwidth=4,bg="white")
Label(f1,text="SALE",bg="silver",font="lucida 20 bold",padx=82).pack()
f1.place(x=810 ,y=65)

f1 = Frame(root,relief=SUNKEN,borderwidth=4,bg="white")
Label(f1,text="CLOSING STOCK",bg="silver",font="lucida 20 bold",padx=11).pack()
f1.place(x=1059 ,y=65)

# quantity raate

f1 = Frame(root,relief=SUNKEN,borderwidth=3,bg="white")
Label(f1,text="Quan",bg="silver",font="lucida 20 bold",padx=21).pack()
f1.place(x=302 ,y=115)

f1 = Frame(root,relief=SUNKEN,borderwidth=3,bg="white")
Label(f1,text="Rate",bg="silver",font="lucida 20 bold",padx=30).pack()
f1.place(x=427 ,y=115)

f1 = Frame(root,relief=SUNKEN,borderwidth=3,bg="white")
Label(f1,text="Quan",bg="silver",font="lucida 20 bold",padx=21).pack()
f1.place(x=562 ,y=115)

f1 = Frame(root,relief=SUNKEN,borderwidth=3,bg="white")
Label(f1,text="Rate",bg="silver",font="lucida 20 bold",padx=30).pack()
f1.place(x=680 ,y=115)

f1 = Frame(root,relief=SUNKEN,borderwidth=3,bg="white")
Label(f1,text="Quan",bg="silver",font="lucida 20 bold",padx=21).pack()
f1.place(x=812 ,y=115)

f1 = Frame(root,relief=SUNKEN,borderwidth=3,bg="white")
Label(f1,text="Rate",bg="silver",font="lucida 20 bold",padx=28).pack()
f1.place(x=930 ,y=115)

f1 = Frame(root,relief=SUNKEN,borderwidth=3,bg="white")
Label(f1,text="Quan",bg="silver",font="lucida 20 bold",padx=25).pack()
f1.place(x=1062 ,y=115)

f1 = Frame(root,relief=SUNKEN,borderwidth=3,bg="white")
Label(f1,text="Rate",bg="silver",font="lucida 20 bold",padx=30).pack()
f1.place(x=1190 ,y=115)

pr = StringVar()
opq = IntVar()
opr = IntVar()
puq = IntVar()
pur = IntVar()
sq = IntVar()
sr = IntVar()
csq = IntVar()
csr = IntVar()


#TEXT
prframe  = Frame(second_frame,relief=SUNKEN,borderwidth=1)
prframe.grid(row=0 , column=0,padx=(0,10))
opqframe = Frame(second_frame,relief=SUNKEN,borderwidth=1)
opqframe.grid(row=0 , column=1,padx=(0,15))
oprframe = Frame(second_frame,relief=SUNKEN,borderwidth=1)
oprframe.grid(row=0 , column=2)
puqframe = Frame(second_frame,relief=SUNKEN,borderwidth=1)
puqframe.grid(row=0 , column=3,padx=(25,8))
purframe = Frame(second_frame,relief=SUNKEN,borderwidth=1)
purframe.grid(row=0 , column=4)
sqframe  = Frame(second_frame,relief=SUNKEN,borderwidth=1)
sqframe.grid(row=0 , column=5,padx=(21,7))
srframe  = Frame(second_frame,relief=SUNKEN,borderwidth=1)
srframe.grid(row=0 , column=6)
csqframe = Frame(second_frame,relief=SUNKEN,borderwidth=1)
csqframe.grid(row=0 , column=7,padx=(20,18))
csrframe = Frame(second_frame,relief=SUNKEN,borderwidth=1)
csrframe.grid(row=0 , column=8)

prentry = Entry(prframe  ,textvariable=pr,font="rockwell 20 bold",width=19)
prentry.grid(row=0 , column=0)
prentry.bind('<Return>',lk1)

opqentry = Entry(opqframe ,textvariable=opq,font="rockwell 20 bold",width=7)
opqentry.grid(row=0 , column=1)
opqentry.bind('<Return>',lk2)

oprentry = Entry(oprframe ,textvariable=opr,font="rockwell 20 bold",width=7)
oprentry.grid(row=0 , column=2)
oprentry.bind('<Return>',lk3)

puqentry = Entry(puqframe ,textvariable=puq,font="rockwell 20 bold",width=7)
puqentry.grid(row=0 , column=3)
puqentry.bind('<Return>',lk4)

purentry = Entry(purframe ,textvariable=pur,font="rockwell 20 bold",width=7)
purentry.grid(row=0 , column=4)
purentry.bind('<Return>',lk5)

sqentry = Entry(sqframe  ,textvariable=sq,font="rockwell 20 bold",width=7)
sqentry.grid(row=0 , column=5)
sqentry.bind('<Return>',lk6)

srentry = Entry(srframe  ,textvariable=sr,font="rockwell 20 bold",width=7)
srentry.grid(row=0 , column=6)
srentry.bind('<Return>',lk7)

csqentry = Entry(csqframe ,textvariable=csq,font="rockwell 20 bold",width=7)
csqentry.grid(row=0 , column=7)
csqentry.bind('<Return>',lk8)

csrentry = Entry(csrframe ,textvariable=csr,font="rockwell 20 bold",width=7)
csrentry.grid(row=0 , column=8)
csrentry.bind('<Return>',lk9)


root.mainloop()