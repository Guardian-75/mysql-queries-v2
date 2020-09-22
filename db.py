class db:
	def __init__(self, Name, Password):
	    self.Name = Name
	    self.Password = Password

	def create_db(self):
		import mysql.connector

		mydb = mysql.connector.connect(
			host = "localhost",
			user = self.Name,
			password = self.Password
			)

		db_name = str(input("\nEnter Your Database Name : "))
		creat_db_query = "CREATE DATABASE " + db_name

		mycursor = mydb.cursor()
		mycursor.execute(creat_db_query)
		print("\n")
		mycursor.execute("SHOW DATABASES")

		for x in mycursor:
			print(x)

		mycursor.close()
		mydb.close()

	def create_tb(self):
		import mysql.connector

		db_name = str(input("Database Name : "))

		mydb = mysql.connector.connect(
			host="localhost",
			user=self.Name,
			password=self.Password,
			database=db_name
		)

		table_name = str(input(" Table Name : "))
		column_name = str(input(" Column Name and Information : "))
		table_queries = " create table {} ({}) ".format(table_name,column_name)

		print(table_queries)

		mycursor = mydb.cursor()
		mycursor.execute(table_queries)
		mycursor.execute("SHOW TABLES")

		for x in mycursor:
			print(x)

		mycursor.close()
		mydb.close()


Name = str(input(" Database User Name : "))
Password = str(input(" Password : "))

	d1 = db(Name, Password)
	d1.create_db()
	d1.create_tb()