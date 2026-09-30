import tkinter as tk
from tkinter import *

win = tk.Tk()


page1 = Frame(win)
page2 = Frame(win)
page3 = Frame(win)

page1.grid(row=0, column=0)
page2.grid(row=0, column=0)
page3.grid(row=0, column=0)

dih = Label(page1, text="dih1")
dih2 = Label(page2, text="dih2")
dih3 = Label(page3, text="dih3")

win.geometry("650x650")

btn1 = Button(page1,
              text="Click Me!",
              font=('Arial', 16, 'bold'),
              command=lambda: page2
              )
btn1.pack()

btn2 = Button(page2,
              text="Click Me!",
              font=('Arial', 16, 'bold'),
              command=lambda: page3
              )
btn2.pack()

page1.tkraise()
win.mainloop()