import tkinter as tk
from tkinter import messagebox
mainWindow=tk.Tk()

l1=tk.Label(master=mainWindow,text='Num1')
l1.pack( side = 'left')
E1 = tk.Entry(master=mainWindow)
E1.pack(side = 'left')

l2=tk.Label(master=mainWindow,text='Num2')
l2.pack( side = 'left')
E2 = tk.Entry(master=mainWindow)
E2.pack(side = 'left')
var = tk.StringVar()
msg = tk.Message( master=mainWindow, textvariable=var )
def addNum():
    c=int(E1.get())+int(E2.get())
    var.set(c)
    msg.pack(side='left')
    tk.messagebox.showinfo("The sum is", c)
B1=tk.Button(master=mainWindow,text='ADD',command=addNum, relief='flat')

B1.pack(side='bottom')
mainWindow.mainloop()
