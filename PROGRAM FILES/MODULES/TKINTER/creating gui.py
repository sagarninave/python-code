import tkinter as samy
from tkinter import messagebox
mainWindow=samy.Tk()

l1=samy.Label(master=mainWindow,text='Enter digit',bg='pink',fg='blue')
l1.pack(side='left')
E1=samy.Entry(master=mainWindow,bg='orange',fg='blue')
E1.pack(side='left')
l2=samy.Label(master=mainWindow,text='Enter digit',bg='pink',fg='blue')
l2.pack(side='left')
E2=samy.Entry(master=mainWindow,bg='orange',fg='blue')
E2.pack(side='left')
var=samy.StringVar()
msg=samy.Message(master=mainWindow, textvariable=var)
def addNum():
        c=int(E1.get())+int(E2.get())
        var.set(c)
        msg.pack(side='left')
        samy.messagebox.showinfo("The sum is ",c)
B1=samy.Button(master=mainWindow,text='ADD',command=addNum,relief='raised',bg='yellow',fg='red',font='Arial 12 bold')
B1.pack(side='bottom')
mainWindow.mainloop()
