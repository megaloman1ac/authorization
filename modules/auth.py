from tkinter import *
from tkinter import messagebox
import sqlite3

def authn(login, password, con, cur):
	
	cmd = f" select * from persons where login = '{login}' and pass = '{password}' "
	
	cur.execute(cmd)
	
	if len(cur.fetchall()) > 0:
		messagebox.showinfo(title='Oh, Yeah!', message='This is happening!')
		return 1
	else:
		messagebox.showinfo(title='Oh no...', message='This isn\'t happening...')
		return 0
