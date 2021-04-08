# -*- coding: utf-8 -*-
"""
Created on Thu Apr  8 21:07:44 2021

@author: 江成丰
"""
from tkinter import *

root = Tk()
root.geometry("700x700") 
root.title("hw1")

def run1():
     a = float(inp1.get())
     s = '%0.2f' % (a)
     txt.insert(END, s)   # 追加显示运算结果
     inp1.delete(0, END)  # 清空输入

lb1 = Label(root, text='输入并显示')
lb1.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.1)

inp1 = Entry(root)
inp1.place(relx=0.35, rely=0.2, relwidth=0.3, relheight=0.1)

btn1 = Button(root, text='点击', command=run1)
btn1.place(relx=0.35, rely=0.4, relwidth=0.3, relheight=0.1)

txt = Text(root)
txt.place(rely=0.6, relwidth=1,relheight=0.4)

root.mainloop()

