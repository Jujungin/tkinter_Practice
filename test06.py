# log-in program with tkinter

import tkinter as tk
from tkinter import messagebox

# create the window
root = tk.Tk()
root.geometry('200x150')

# create the menu
main_menu = tk.Menu(root)
root.config(menu=main_menu)

# create the file menu
file_menu = tk.Menu(main_menu, tearoff=False)
main_menu.add_cascade(label='File', menu=file_menu)

# create the file menu items
file_menu.add_command(label='Quit', command=root.quit)

# create the help menu
help_menu = tk.Menu(main_menu, tearoff=False)
main_menu.add_cascade(label='Help', menu=help_menu)

# create the help menu items
help_menu.add_command(label='About', command=lambda: messagebox.showinfo(
    title='About',
    message='This is a simple login program'
))

# create the login frame
login_frame = tk.Frame(root)
login_frame.pack()

# create the username label
username_label = tk.Label(login_frame, text='Username')
username_label.grid(row=0, column=0)

# create the username entry
username_entry = tk.Entry(login_frame)
username_entry.grid(row=0, column=1)

# create the password label
password_label = tk.Label(login_frame, text='Password')
password_label.grid(row=1, column=0)

# create the password entry
password_entry = tk.Entry(login_frame, show='*')
password_entry.grid(row=1, column=1)

# create the login button
login_button = tk.Button(login_frame, text='Login')
login_button.grid(row=2, column=0, columnspan=2)

# run the main loop
root.mainloop()

