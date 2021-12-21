from tkinter import *
from tkinter import ttk
import datetime
import pyautogui as pag

def lk1(event):
    pag.click(399,500)

def lk2(event):
    pag.click(532,500)

def lk3(event):
    pag.click(665,500)

def lk4(event):
    pag.click(798,500)

def lk5(event):
    pag.click(931,500)

def lk6(event):
    pag.click(1064,500)

def lk7(event):
    pag.click(1197,500)

def lk8(event):
    pag.click(1330,500)

def lk9(event):
    pag.click(133,500)

root = Tk()

root_length = 1330
root_breath = 690
root_screen_width = root.winfo_screenwidth()
root_screen_height = root.winfo_screenheight()
tdate = datetime.date.today()
wdate = "enable it"
# wdate = intro.date.get()    enable it

root.geometry(f"{root_length}x{root_breath}")
root.resizable(False,True)
x_cordinate = int((root_screen_width/2) - (root_length/2))
y_cordinate = int((root_screen_height/2) - (root_breath-310))
root.geometry("{}x{}+{}+{}".format(root_length, root_breath, x_cordinate, y_cordinate))
root.configure(bg="grey")

main_frame = Frame(root,bg="grey")
main_frame.pack(side = BOTTOM,fill=BOTH)

my_canvas = Canvas(main_frame,height=515,bg="grey")
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

#TEXT
pro_text = Text(second_frame,width=21,height=1000,font="Aharoni 25 bold",bg="grey")
pro_text.grid(row=1,column=0)
pro_text.bind('<Return>',lk1)

op_quan_text = Text(second_frame,width=9,height=1000,font="Aharoni 25 bold",bg="grey")
op_quan_text.grid(row=1,column=1)
op_quan_text.bind('<Return>',lk2)

op_rt_text = Text(second_frame,width=9,height=1000,font="Aharoni 25 bold",bg="grey")
op_rt_text.grid(row=1,column=2)
op_rt_text.bind('<Return>',lk3)

p_quan_text = Text(second_frame,width=9,height=1000,font="Aharoni 25 bold",bg="grey")
p_quan_text.grid(row=1,column=3)
p_quan_text.bind('<Return>',lk4)

p_rt_text = Text(second_frame,width=9,height=1000,font="Aharoni 25 bold",bg="grey")
p_rt_text.grid(row=1,column=4)
p_rt_text.bind('<Return>',lk5)

s_quan_text = Text(second_frame,width=9,height=1000,font="Aharoni 25 bold",bg="grey")
s_quan_text.grid(row=1,column=5)
s_quan_text.bind('<Return>',lk6)

s_rt_text = Text(second_frame,width=8,height=1000,font="Aharoni 25 bold",bg="grey")
s_rt_text.grid(row=1,column=6)
s_rt_text.bind('<Return>',lk7)

cs_quan_text = Text(second_frame,width=9,height=1000,font="Aharoni 25 bold",bg="grey")
cs_quan_text.grid(row=1,column=7)
cs_quan_text.bind('<Return>',lk8)

cs_rt_text = Text(second_frame,width=9,height=1000,font="Aharoni 25 bold",bg="grey")
cs_rt_text.grid(row=1,column=8)
cs_rt_text.bind('<Return>',lk9)

root.mainloop()