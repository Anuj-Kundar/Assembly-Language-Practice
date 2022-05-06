import tkinter as tk
import numpy as np
import matplotlib.pyplot as plt     #sudo apt-get install python3-matplotlib

root = tk.Tk()

def fn():
    v1 = c1.get()
    v2 = c2.get()
    if v1==1 and v2==0:
        x = np.arange(-2*np.pi,2*np.pi,0.1)
        y = np.sin(x)
        plotting(x,y,y,'Sine')
    elif v2==1 and v1==0:
        x = np.arange(-2*np.pi,2*np.pi,0.1)
        y = np.cos(x)
        plotting(x,y,y,'Cos')
    elif v1==v2==1:
        x = np.arange(-2*np.pi,2*np.pi,0.1)
        y = np.sin(x)
        z = np.cos(x)
        plotting(x,y,z,'Comparison')
    elif v1==v2==0:
        plt.cla()
        plt.grid('on')
        plt.show()
        print('None Option Selected')

def plotting(x,y,z,c):
    plt.cla()
    plt.figure(1)
    plt.plot(x,y,'r',Linewidth=4)
    plt.plot(x,z,'b',Linewidth=4)
    plt.xlabel('range')
    plt.ylabel(c)
    plt.grid('on')
    plt.show()

c1 = tk.IntVar()
c2 = tk.IntVar()
Chk1 = tk.Checkbutton(root,text='Sine',variable=c1)
Chk2 = tk.Checkbutton(root,text='cos',variable=c2)
B1 = tk.Button(root,text = 'Show',command=fn)
Chk1.pack()
Chk2.pack()
B1.pack()

root.mainloop()