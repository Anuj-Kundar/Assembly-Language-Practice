#  Write a python program to understand creation of Layouts, Radiobutton,Check boxes and dialog boxes using Tkinter

import tkinter as tk
root = tk.Tk()


def res():
    v1 = E1.get()
    v1 = int(v1)
    v2 = E2.get()
    v2 = int(v2)
    c = v1+v2
    L3.config(text=str(c))


C = tk.StringVar()
C1 = tk.StringVar()
btn_Result = tk.Button(root, text='Result', command=res)
L1 = tk.Label(root, text='Num1')
L3 = tk.Label(root)
E1 = tk.Entry(root)
L2 = tk.Label(root, text='Num2')
E2 = tk.Entry(root)
L1.grid(row=0, column=0)
E1.grid(row=0, column=1)
L2.grid(row=1, column=0)
E2.grid(row=1, column=1)
btn_Result.grid(row=2, column=0)
L3.grid(row=2, column=1)

root.mainloop()
