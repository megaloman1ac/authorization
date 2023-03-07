import sqlite3

class SQL:
	
	# At first, i've created simple "select" query function 
	def sql_query_select(login, password):
		
		
		# Connection
		connection = sqlite3.connect("users.db")
		cur = connection.cursor()
		
		# Creating and executing a command	
		command = "select * from persons where login = '{0}' and pass = '{1}'".format(login, password)
		cur.execute(command)
		
		
		# Checking for users (if it has row)
		
		if len(cur.fetchall()) > 0:
			return 1
		else:
			return 0
	
	# At first, i've created simpole "insert" query function
	def sql_query_insert(login, password):
		try:
			# Connection
			connection = sqlite3.connect("users.db")
			cur = connection.cursor()
			
			# Creating and executing a command	
			command = "insert into persons values ('{0}', '{1}')".format(login, password)
			cur.execute(command)
			
			# Add user to DB
			connection.commit()
			
			# Return 1 if it OK
			return 1
		except ValueError:
			return 0
				 
		
