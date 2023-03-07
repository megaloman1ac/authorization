from tkinter import messagebox
import hashlib
from modules.auth import *
import sqlite3


def regstr(login, password):
	
	if login.strip() == "" and password.strip() == "":
		messagebox.showinfo(title='Nothing', message='you wrote nothing')
	elif login.strip() == "":
		messagebox.showinfo(title='No login', message='No login was written')
	elif password.strip() == "":
		messagebox.showinfo(title='No pass', message='No password was written')
	else:
		sha256 = hashlib.sha256()
		
		sha256.update(password.encode('utf8'))
		
		try:	
			res = SQL.sql_query_insert(login, sha256.hexdigest())
			if res == 1:
				return 1
			else:
				return 0
			messagebox.showinfo(title='Horray', message='You have been regisrated!')

		except ValueError:
			messagebox.showinfo(title='Oh no', message='something went wrong...')
			return 0;
