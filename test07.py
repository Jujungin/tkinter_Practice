import tkinter as tk
from tkinter import messagebox

see_more = messagebox.askyesno(
    title = 'See more',
    message='Would you like to see another box?',
    detail='Click No to quit'
)

if not see_more:
    exit()

messagebox.showinfo(
    title = 'You got it',
    message="Ok, here's another dialog.",
    detail='hope you like it'
)

