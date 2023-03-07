from tkinter import messagebox
import hashlib
from modules.auth import *
import sqlite3


def regstr(login, password, con, cur):
	
	if login.strip() == "" and password.strip() == "":
		messagebox.showinfo(title='Nothing', message='you wrote nothing')
	elif login.strip() == "":
		messagebox.showinfo(title='No login', message='No login was written')
	elif password.strip() == "":
		messagebox.showinfo(title='No pass', message='No password was written')
	else:
		pwd = hashlib.sha256()
		
		pwd.update(password.encode('utf8'))
		
		try:
			cmd = f" insert into persons (login, pass) values ('{login}', '{pwd.hexdigest()}')"
	
			cur.execute(cmd)
			messagebox.showinfo(title='Horray', message='You have been regisrated!')
			con.commit()
			return 1;
		except ValueError:
			messagebox.showinfo(title='Oh no', message='something went wrong...')
			return 0;
