import sqlite3

class SQL:
	
	# At first, i've created simple "select" query function 
	def sql_query_select(login, password):
		
		connection = sqlite3.connect("users.db")
		cur = connection.cursor()
				
		command = "select * from persons where login = '{0}' and pass = '{1}'".format(login, password)
		cur.execute(command)
		
		if len(cur.fetchall()) > 0:
			return 1
		else:
			return 0
	
	# At first, i've created simpole "insert" query function
	def sql_query_insert(login, password):
		try:
			connection = sqlite3.connect("users.db")
			cur = connection.cursor()
		
			command = "insert into persons values ('{0}', '{1}')".format(login, password)
			cur.execute(command)
		
			connection.commit()
			return 1
		except ValueError:
			return 0
				 
		
