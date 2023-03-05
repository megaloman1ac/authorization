#!/usr/bin/python3

from tkinter import *
from tkinter import messagebox
import sqlite3

def btn_click():
	l = login.get()
	p = psd.get()
	
	cmd = f" select * from persons where login = '{l}' and pass = '{p}' "
	
	cur.execute(cmd)
	
	if len(cur.fetchall()) > 0:
		messagebox.showinfo(title='Oh, Yeah!', message='This is happening!')
		log.config(text = f"Login: {l}")
		ps.config(text = f"Pass: {p}")
	else:
		messagebox.showinfo(title='Oh no...', message='This isn\'t happening...')


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
