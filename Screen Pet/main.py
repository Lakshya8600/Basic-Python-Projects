from tkinter import *
import time 

root = Tk()
root.title("Screen Pet - Tommy")
root.geometry("400x350")
root.configure(bg="blue")
root.resizable(False,False)
bodycolour = "green"

c = Canvas(root,height=350,width=400,bg="light blue")
c.pack()

leg1 = c.create_oval(50,300,200,330,fill=bodycolour,outline=bodycolour)
leg2 = c.create_oval(200,330,350,300,fill=bodycolour,outline=bodycolour)
body = c.create_oval(30,30,370,320,fill=bodycolour,outline=bodycolour)
eye1 = c.create_oval(130,70,180,150)
eye2 = c.create_oval(210,70,265,150)
c.create_line(180,150,190,160,200,170)
# c.create_line(200,200,200,20,fill="red")
# eye1 = c.create_oval(130,70,180,150)
# eye2 = c.create_oval(210,70,265,150)



root.mainloop()