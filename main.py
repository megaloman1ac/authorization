#!/usr/bin/python3

from tkinter import *
from tkinter import messagebox
from modules.auth import *


def btn_click():
	log_in = authn(login.get(), psd.get(), con, cur)
	
	if log_in == 0:
		print("Nothing to do...")
	else:
		print("Work was found!")
		log.config(text = f"Login: {login.get()}")
		ps.config(text = f"Pass: {psd.get()}")
	


# sqlite
con = sqlite3.connect('users.db')

cur = con.cursor()

# Main root
root = Tk()

root.title('authorization')
root.geometry('300x400')

root.resizable(width=False, height=False)


# Canvas and Frame
canvas = Canvas(root, height=400, width=250)
canvas.pack()

frame = Frame(root, bg='grey')

frame.place(relwidth=1, relheight=1)


# Elements
title = Label(frame, text='Authorization', bg='grey')
btn = Button(frame, text='Click', command=btn_click)
login = Entry(frame)
psd = Entry(frame, show="*")

global log
global ps
log = Label(frame, text='', bg='grey')
ps = Label(frame, text='', bg='grey')


# Packs
title.pack()
login.pack()
psd.pack()
btn.pack()
log.pack()
ps.pack()

# sqlite commit
con.commit()

root.mainloop()
