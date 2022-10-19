# practise git : https://github.com/PacktPublishing/Python-GUI-Programming-Cookbook-Third-Edition


# docs : https://docs.python.org/3/library/tkinter.html
from argparse import Action
from faulthandler import disable
import tkinter as tk

# Ttk comes with 18 widgets, twelve of which already existed in tkinter:
# Button, Checkbutton, Entry, Frame, Label, LabelFrame, Menubutton, PanedWindow, Radiobutton, Scale, Scrollbar, and Spinbox. 
# The other six are new: Combobox, Notebook, Progressbar, Separator, Sizegrip and Treeview. And all them are subclasses of Widget.
# docs : https://docs.python.org/3/library/tkinter.ttk.html
from tkinter import Label, ttk
from turtle import width

from pandas import wide_to_long
from sqlalchemy import column
from sympy import radsimp


win = tk.Tk()
win.title("GUI")

# disable resize 
# resizable(x dimension, y dimension)
#win.resizable(False,False)

# able resize, this is default value
win.resizable(True,True)



#########
# row=0 #
#########
a_label = ttk.Label(win, text=" A Label ")
a_label.grid(column=0, row=0)


def click_me_1():
    action1.configure(text="**i have been clicked**")
    # change color after click event
    a_label.configure(foreground="red")
    # change text after click event
    a_label.configure(text="A red label")
    action1.configure(state="disabled")

# command parameter is define function name
action1 = ttk.Button(win, text="click me", command=click_me_1)
action1.grid(column=1, row=0)



#########
# row=1 #
# row=2 #
#########
def click_me_name():
    action2.configure(text='Hello ' + name.get())

action2 = ttk.Button(win, text="click me 2", command=click_me_name)
action2.grid(column=1, row=2)
ttk.Label(win, text="Enter a name : ").grid(column=0, row=1)

name = tk.StringVar()
name_entered = ttk.Entry(win, width=12, textvariable=name)
name_entered.grid(column=0, row=2)

# Place cursor into name Entry then first start GUI
name_entered.focus()



#########
# row=3 #
# row=4 #
#########
def click_me_name_combo():
    action3.configure(text='Hello ' + name_combo.get() + ', Your choosen number is ' + number.get())

name_combo = tk.StringVar()
name_combo_entered = ttk.Entry(win, width=12, textvariable=name_combo)
name_combo_entered.grid(column=0, row=4)

action3 = ttk.Button(win, text="click me 3", command=click_me_name_combo)
action3.grid(column=2, row=4)

ttk.Label(win, text="Enter a name : ").grid(column=0, row=3)
ttk.Label(win, text="Choose a number : ").grid(column=1, row=3)
number = tk.StringVar()
number_choosen = ttk.Combobox(win, width=12, textvariable=number)
number_choosen['values'] = (1,2,4,42,100)
number_choosen.grid(column=1, row=4)
number_choosen.current(0)


#########
# row=5 #
# row=6 #
# row=7 # check box
#########


def click_me_namve_combo2():
    action4.configure(text='Hello ' + name_combo2.get() + ', Your choosen number is ' + number2.get())

ttk.Label(win, text="Enter a name : ").grid(column=0, row=5)
ttk.Label(win, text="Choose a number : ").grid(column=1, row=5)

action4 = ttk.Button(win, text="click me 4", command=click_me_namve_combo2)
action4.grid(column=2, row=6)

name_combo2 = tk.StringVar()
name_combo2_entered = ttk.Entry(win, width=12, textvariable=name_combo2)
name_combo2_entered.grid(column=0,row=6)

number2 = tk.StringVar()
number2_choosen = ttk.Combobox(win, width=12, textvariable=number2)
number2_choosen['values'] = (10,20,40,420,1000)
number2_choosen.grid(column=1, row=6)
number2_choosen.current(0)

#check box
chVarDis = tk.IntVar()
check1 = tk.Checkbutton(win, text="Disable", variable=chVarDis, state='disabled')
check1.select()
check1.grid(column=0, row=7, sticky=tk.W)

chVarUn = tk.IntVar()
check2 = tk.Checkbutton(win, text="UnChecked", variable=chVarUn)
check2.select()
check2.grid(column=1, row=7, sticky=tk.W)

chVarEn = tk.IntVar()
check3 = tk.Checkbutton(win, text="Enabled", variable=chVarEn)
check3.select()
check3.grid(column=2, row=7, sticky=tk.E)

name_combo2_entered.focus()


##########
# row=8  #
##########

COLOR1 = "Blue"
COLOR2 = "Gold"
COLOR3 = "Red"

def radCall():
    radSel = radVar.get()
    if radSel == 1:
        win.configure(background=COLOR1)
    elif radSel == 2:
        win.configure(background=COLOR2)
    elif radSel ==3:
        win.configure(background=COLOR3)


radVar = tk.IntVar()
rad1 = tk.Radiobutton(win, text=COLOR1, variable=radVar, value=1, command=radCall)
rad1.grid(column=0, row=8, sticky=tk.W, columnspan=3)

rad2 = tk.Radiobutton(win, text=COLOR2, variable=radVar, value=2, command=radCall)
rad2.grid(column=1, row=8, sticky=tk.W, columnspan=3)

rad3 = tk.Radiobutton(win, text=COLOR3, variable=radVar, value=3, command=radCall)
rad3.grid(column=2, row=8, sticky=tk.W, columnspan=3)


##########
# row=8  #
##########
# create radiobutton in one loop
colors = ["Black", "Yellow", "Green"]

def radCall2():
    radSel2 = radVar2.get()
    if radSel2 == 0:
        win.configure(background=colors[0])
    elif radSel2 == 1:
        win.configure(background=colors[1])
    elif radSel2 == 2:
        win.configure(background=colors[2])


radVar2 = tk.IntVar()

radVar2.set(99)

for col in range(len(colors)):
    curRad = tk.Radiobutton(win, text=colors[col], variable=radVar2, value=col, command=radCall2)
    curRad.grid(column=col, row=9, sticky=tk.W)




##########
# row=10  #
##########
# scrolled text widget

from tkinter import scrolledtext

scroll_w = 40
scroll_h = 3
scr = scrolledtext.ScrolledText(win, width=scroll_w, height=scroll_h, wrap=tk.WORD)
scr.grid(column=0, columnspan=3)



#################
#   start GUI   #
#################
win.mainloop()