from tkinter import *
from PIL import Image,ImageTk
import random
#variables
colour = "black"
fcolour = "white"
text1 = "."
text2 = "."
text3 = "."
text4 = "."
text5 = "."
text6 = "."
text7 = "."
text8 = "."
text9 = "."
r1 = 0
r2 = 0
r3 = 0
r4 = 0
r5 = 0
r6 = 0
r7 = 0
r8 = 0
r9 = 0

rc1 = 0
rc2 = 0
rc3 = 0
rc4 = 0
rc5 = 0
rc6 = 0
rc7 = 0
rc8 = 0
rc9 = 0
turn = 1

#functions
def des():
    intro.destroy()

def b1():
    b1.configure(text="X",fg="red")
    global r1
    r1 = 1
    global turn
    turn += 1

def b2():
    b2.configure(text="X",fg="red")
    global r2
    r2 = 1
    global turn
    turn += 1


def b3():
    global r3
    b3.configure(text="X",fg="red")
    r3 = 1
    global turn
    turn += 1

def b4():
    global r4
    b4.configure(text="X",fg="red")
    r4 = 1
    global turn
    turn += 1

def b5():
    global r5
    b5.configure(text="X",fg="red")
    r5 = 1
    global turn
    turn += 1

def b6():
    global r6
    b6.configure(text="X",fg="red")
    r6 = 1
    global turn
    turn += 1

def b7():
    global r7
    b7.configure(text="X",fg="red")
    r7 = 1
    global turn
    turn += 1

def b8():
    global r8
    b8.configure(text="X",fg="red")
    r8 = 1
    global turn
    turn += 1

def b9():
    global r9
    b9.configure(text="X",fg="red")
    r9 = 1
    global turn
    turn += 1

# global rc1
# global rc2
# global rc3
# global rc4
# global rc5
# global rc6
# global rc7
# global rc8
# global rc9

def update():
    if turn == 2:
        if r5 == 0:
            b5.configure(text="O",fg="yellow")
            global rc5
            rc5 = 1
            print(r5)

        else:
            a = random.randint(1,4)
            if a == 1:
                b1.configure(text="O", fg="yellow")
                global rc1
                rc1 = 1


            elif a==2:
                b3.configure(text="O", fg="yellow")
                global rc3
                rc3 = 1

            elif a==3:
                b7.configure(text="O", fg="yellow")
                global rc7
                rc7 = 1

            else:
                b9.configure(text="O", fg="yellow")
                global rc9
                rc9 = 1

    elif turn==3:
        if r5 == 0:
            if r1==1 and r3==1:
                b2.configure(text="O", fg="yellow")
                global rc2
                rc2 = 1

            elif r1==1 and r7==1:
                b4.configure(text="O", fg="yellow")
                global rc4
                rc4 = 1

            elif r3==1 and r9==1:
                b6.configure(text="O", fg="yellow")
                global rc6
                rc6 = 1

            elif r7==1 and r9==1:
                b8.configure(text="O", fg="yellow")
                global rc8
                rc8 = 1

            elif r2==1 and r4==1:
                b1.configure(text="O", fg="yellow")
                # global rc1
                rc1 = 1

            elif r2==1 and r4==6:
                b3.configure(text="O", fg="yellow")
                # global rc3
                rc3 = 1

            elif r4==1 and r8==1:
                b7.configure(text="O", fg="yellow")
                # global rc7
                rc7 = 1

            elif r6==1 and r8 == 1:
                b9.configure(text="O", fg="yellow")
                # global rc9
                rc9 = 1

            elif r1==1 and r2==1:
                b3.configure(text="O", fg="yellow")
                # global rc3
                rc3 = 1

            elif r2==1 and r3==1:
                b1.configure()
                # global rc1
                rc1 = 1

            else:
                a = random.randint(1,4)
                if a==1:
                    b2.configure(text="O", fg="yellow")
                    # global rc2
                    rc2 = 1

                elif a==2:
                    b4.configure(text="O", fg="yellow")
                    # global rc4
                    rc4 = 1

                elif a==3:
                    b6.configure(text="O", fg="yellow")
                    # global rc6
                    rc6 = 1

                else:
                    b8.configure(text="O", fg="yellow")
                    # global rc3
                    rc3 = 1


        elif r5==1 :
            if r1==1:
                b9.configure(text="O", fg="yellow")
                # global rc9
                rc9 = 1

            elif r2 == 1:
                b8.configure(text="O", fg="yellow")
                # global rc8
                rc8 = 1

            elif r3 == 1:
                b7.configure(text="O", fg="yellow")
                # global rc7
                rc7 = 1

            elif r4 == 1:
                b6.configure(text="O", fg="yellow")
                # global rc6
                rc6 = 1

            elif r6 == 1:
                b4.configure(text="O", fg="yellow")
                # global rc4
                rc4 = 1

            elif r7 == 1:
                b3.configure(text="O", fg="yellow")
                # global rc3
                rc3 = 1

            elif r8 == 1:
                b2.configure(text="O", fg="yellow")
                # global rc2
                rc2 = 1

            elif r9 == 1:
                b1.configure(text="O", fg="yellow")
                # global rc1
                rc1 = 1


    elif turn==4:
        if r5==1:
            lst1 = [[rc1,rc3,r2,rc2,b2],[rc3,rc9,r6,rc6,b6],[rc7,rc9,r8,rc8,b8],[rc1,rc7,r4,rc4,b4]]
            for a,b,c,d,e in lst1:
                if a==1 and b==1:
                    if c==0:
                        e.configure(text="O",fg="yellow")
                        d = 1

                    else:
                        lst2 = [[1, b1, rc1, r1]]
                        for x, y, z, v in lst2:
                            a = random.randint(1,8)


                            if a==x and v!=1:
                                y.configure(text="O",fg="yellow")
                                z = 1
                                break






intro = Tk()

window_length = 500
window_breath = 289
intro.geometry(f"{window_length}x{window_breath}")

screen_width = intro.winfo_screenwidth()
screen_height = intro.winfo_screenheight()
intro.title("TIK TAK TOE GAME")

# Screen Size
intro.resizable(False,False)
x_cordinate = int((screen_width/2) - (window_length/2))
y_cordinate = int((screen_height/2) - (window_breath/2))
intro.geometry("{}x{}+{}+{}".format(window_length, window_breath, x_cordinate, y_cordinate))
intro.configure(bg="violet")

can = Canvas(intro,width=474)
can.place(x=10,y=10)
can.configure(bg="orange")

photo = Image.open("photo.jpg")
pic = ImageTk.PhotoImage(image=photo)
Label(intro,image=pic).place(x=12,y=10)

lk = Image.open("lk.jpg")
lkpic = ImageTk.PhotoImage(image=lk)
Label(intro,image=lkpic).place(x=12,y=140)

yash = Image.open("yash.jpg")
yashpic = ImageTk.PhotoImage(image=yash)
Label(intro,image=yashpic).place(x=375,y=140)

Label(intro,text="TIK TAK TOE",font="algerian 25 bold",bg="orange").place(x=140,y=120)

f = Frame(intro,relief= SUNKEN, borderwidth=6)
f.place(x=190,y=170)
b = Button(f,text="Start",font="Courgette 20 bold",bg="orchid",command=des)
b.pack()

intro .mainloop()
from tkinter import *

root = Tk()
window_length = 500
window_breath = 500
root.geometry(f"{window_length}x{window_breath}")



screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
root.title("TIK TAK TOE GAME")

# Screen Size
root.resizable(False, False)
x_cordinate = int((screen_width / 2) - (window_length / 2))
y_cordinate = int((screen_height / 2) - (window_breath / 2))
root.geometry("{}x{}+{}+{}".format(window_length, window_breath, x_cordinate, y_cordinate))
root.configure(bg=colour)

    #frame
f = Frame(root,borderwidth=5,padx=30,bg=colour)
f.grid(row=0 ,column=0)
b1 = Button(f,text=text1,font="elephant 40 bold",borderwidth=0,bg=colour,fg=fcolour,command=b1)
b1.pack()

f = Frame(root, borderwidth=5,padx=40,bg=colour)
f.grid(row=0, column=1)
b2 = Button(f, text=text2, font="elephant 40 bold",borderwidth=0,bg=colour,fg=fcolour,command=b2)
b2.pack()

f = Frame(root, borderwidth=5,padx=40,bg=colour)
f.grid(row=0, column=2)
b3 = Button(f, text=text3, font="elephant 40 bold",fg=fcolour,borderwidth=0,bg=colour,command=b3)
b3.pack()

f = Frame(root, borderwidth=5,bg=colour)
f.grid(row=1, column=0)
b4 = Button(f, text=text4, font="elephant 40 bold",fg=fcolour,borderwidth=0,bg=colour,command=b4)
b4.pack()

f = Frame(root, borderwidth=5,bg=colour)
f.grid(row=1, column=1)
b5 = Button(f, text=text5, font="elephant 40 bold",fg=fcolour,borderwidth=0,bg=colour,command=b5)
b5.pack()

f = Frame(root, borderwidth=5,bg=colour)
f.grid(row=1, column=2)
b6 = Button(f, text=text6, font="elephant 40 bold",borderwidth=0,bg=colour,fg=fcolour,command=b6)
b6.pack()

f = Frame(root, borderwidth=5,bg=colour)
f.grid(row=2, column=0)
b7 = Button(f, text=text7, font="elephant 40 bold",borderwidth=0,bg=colour,fg=fcolour,command=b7)
b7.pack()

f = Frame(root, borderwidth=5,bg=colour)
f.grid(row=2, column=1)
b8 = Button(f, text=text8, font="elephant 40 bold",borderwidth=0,bg=colour,fg=fcolour,command=b8)
b8.pack()

f = Frame(root, borderwidth=5,bg=colour)
f.grid(row=2, column=2)
b9 = Button(f, text=text9, font="elephant 40 bold",borderwidth=0,bg=colour,fg=fcolour,command=b9)
b9.pack()

f = Frame(root, borderwidth=5,bg=colour)
f.grid(row=3, column=1)
b10 = Button(f, text="done", font="elephant 40 bold",borderwidth=0,bg="violet" ,fg=fcolour,command=update,activebackground="light blue",activeforeground="green")
b10.pack()




root.mainloop()



