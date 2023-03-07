#!/usr/bin/python3

from tkinter import *
from tkinter import messagebox
import sqlite3
from modules.auth import *
from modules.reg import *


def login_click():
	log_in = authn(login.get(), psd.get(), con, cur)
	
	if log_in == 0:
		print("Nothing to do...")
	else:
		print("Work was found!")
		log.config(text = f"Login: {login.get()}")
		ps.config(text = f"Pass: {psd.get()}")

def reg_click():
	reg = regstr(login.get(), psd.get(), con, cur)
	
	if reg == 0:
		print("OH-NO!")
	elif reg == 1:
		print("System: Long time no see, my loathsome copy!")


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


#### Elements #####

### Labels

# Title
title = Label(frame, text='Authorization', bg='grey')

# User info
log = Label(frame, text='', bg='grey')
ps = Label(frame, text='', bg='grey')

### Buttons

log_in = Button(frame, width='17', text='Log in', command=login_click)
reg_me = Button(frame, width='17', text='Registration', command=reg_click)

### Entries
login = Entry(frame)
psd = Entry(frame, show="*")




# Packs
title.pack()
login.pack()
psd.pack()
log_in.pack()
reg_me.pack()
log.pack()
ps.pack()

# sqlite commit
con.commit()

root.mainloop()
