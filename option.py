def Auto():
	pass

def Manual():

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

			mycursor = mydb.cursor()
			mycursor.execute(table_queries)
			print("\n")
			mycursor.execute("SHOW TABLES")

			for x in mycursor:
				print(x)

			mycursor.close()
			mydb.close()

		def show_db(self):
			import mysql.connector
			
			mydb = mysql.connector.connect(
				host="localhost",
				user=self.Name,
				password=self.Password
			)

			mycursor = mydb.cursor()
			print("\n")
			mycursor.execute("SHOW DATABASES")

			for x in mycursor:
				print(x)

			mycursor.close()
			mydb.close()


		def show_tb(self):
			import mysql.connector

			db_name = str(input("Database Name : "))

			mydb = mysql.connector.connect(
				host="localhost",
				user=self.Name,
				password=self.Password,
				database=db_name
			)

			mycursor = mydb.cursor()
			print("\n")
			mycursor.execute("SHOW TABLES")

			for x in mycursor:
				print(x)

			mycursor.close()
			mydb.close()



	Name = str(input(" Database User Name : "))
	Password = str(input(" Password : "))

	d1 = db(Name, Password)
	while True:
		option = int(input("\n 1: Create Database		2: Create Table \n 3: Show Databases		4: Show Tables \n 5: Delete Databases		6: Delete Tables \n 7: Input Values		8: Auto \n 9: Exit \n option = "))

		# Create Database
		if option==1:
			d1.create_db()

		# Create Table
		elif option==2:
			d1.create_tb()

		# Show Databases
		elif option==3:
			d1.show_db()

		# Show Tables
		elif option==4:
			d1.show_tb()

		# Delete Databases
		elif option==5:
			break

		# Delete Tables
		elif option==6:
			break

		# Input Values
		elif option==7:
			i = int(input("Column include(1) or not_include(2) : "))

			if i==1:
				include()
			else :
				not_include()

		# Auto
		elif option==7:
			break

		# Exit
		elif option==7:
			break
		

if __name__ == "__main__":

	Start = int(input(" 1: Auto		2: Manual \n Option = "))

	if Start==1:
		Auto()

	elif Start==2:
		Manual()

