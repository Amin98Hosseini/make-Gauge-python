from tkinter import *
from tkinter import ttk
import math
import time

master = Tk()
master.geometry("280x250")
master.title("AMIN HOSSEINI")


center_x   = 140
center_y   = 140
radius     = 110



gu1=PhotoImage(file="GUI-Gauge.png")

l1=ttk.Label(master,image=gu1)
l1.pack()
l1.place(x=0,y=0)

w = Canvas(master,width=500, height=500)
w.pack()

d=0


v=w.create_image(140,120, image=gu1)
tc=w.create_line(center_x,center_y,40,140, fill="black", width=2)

def f1():
    global d
    global tc
    w.delete(tc)
    d+=1
    degree = d+180
    degree = math.radians(degree)
    x = radius * math.cos(degree) + center_x
    y = radius * math.sin(degree) + center_y
    tc=w.create_line(center_x,center_y,x,y, fill="black", width=2)
    

b1=Button(master,text="Change")
b1.pack()
b1.place(x=115, y=220)
b1.config(command=f1)

mainloop()
