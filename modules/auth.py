from tkinter import *
from tkinter import messagebox
from modules.sql import *
import hashlib


def authn(login, password):
	
	sha256 = hashlib.sha256()
	
	sha256.update(password.encode('utf8'))

	res = SQL.sql_query_select(login, sha256.hexdigest())
	
	if res == 1:
		messagebox.showinfo(title='Oh, Yeah!', message='This is happening!')
		return 1
	else:
		messagebox.showinfo(title='Oh no...', message='This isn\'t happening...')
		return 0
