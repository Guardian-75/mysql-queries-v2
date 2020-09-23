def Main():

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

			db_name = str(input(" Enter Your Database Name : "))
			creat_db_query = "CREATE DATABASE " + db_name

			mycursor = mydb.cursor()
			mycursor.execute(creat_db_query)
			print("__________________________________________________\n Database List")
			mycursor.execute("SHOW DATABASES")

			for x in mycursor:
				print(x)

			mycursor.close()
			mydb.close()

		def create_tb(self):
			import mysql.connector

			db_name = str(input(" Database Name : "))

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
			print("__________________________________________________\n Table List")
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
			print("__________________________________________________\n Database List")
			mycursor.execute("SHOW DATABASES")

			for x in mycursor:
				print(x)

			print("__________________________________________________")
			mycursor.close()
			mydb.close()


		def show_tb(self):
			import mysql.connector

			db_name = str(input(" Database Name : "))

			mydb = mysql.connector.connect(
				host="localhost",
				user=self.Name,
				password=self.Password,
				database=db_name
			)

			mycursor = mydb.cursor()
			print("__________________________________________________\n Database List")
			mycursor.execute("SHOW TABLES")

			for x in mycursor:
				print(x)

			print("__________________________________________________")
			mycursor.close()
			mydb.close()

		def delete_db(self):
			import mysql.connector

			db_name = str(input(" Database Name : "))

			mydb = mysql.connector.connect(
				host="localhost",
				user=self.Name,
				password=self.Password,
				database=db_name
			)

			mycursor = mydb.cursor()
			mycursor.execute("DROP DATABASE {}".format(db_name))

			for x in mycursor:
				print(x)

			mycursor.close()
			mydb.close()

		def delete_tb(self):
			import mysql.connector

			db_name = str(input(" Database Name : "))
			table_name = str(input(" Table Name : "))

			mydb = mysql.connector.connect(
				host="localhost",
				user=self.Name,
				password=self.Password,
				database=db_name
			)

			mycursor = mydb.cursor()
			mycursor.execute("DROP TABLE {}".format(table_name))

			for x in mycursor:
				print(x)

			mycursor.close()
			mydb.close()

		def input_values(self):
			import re
			import csv
			import mysql.connector

			db_name = str(input(" Database Name : "))
			table_name = str(input(" Table Name : "))
			column_time = int(input(" How many column : "))
			column_name = str(input(" Column Name : "))
			file_name = str(input(" Enter your csv file name : "))

			column_times = "%s "*column_time
			t = column_time-1
			cs = re.sub("\s", ",", column_times, t)

			mydb = mysql.connector.connect(
			  host="localhost",
			  user=self.Name,
			  password=self.Password,
			  database=db_name
			)

			mycursor = mydb.cursor()

			arr=[]
			with open('{}.csv'.format(file_name),'r') as data: 
				for line in csv.reader(data):
			   		t=tuple(line)
			   		print(t)
			   		arr.append(t)

			sql = "INSERT INTO {}({}) VALUES ({})".format(table_name,column_name,cs)
			val = arr

			mycursor.executemany(sql, val) 
			mydb.commit() 

			print(mycursor.rowcount, "details inserted") 
			mydb.close()




	Name = str(input(" Database User Name : "))
	Password = str(input(" Password : "))

	d1 = db(Name, Password)
	while True:
		option = int(input("__________________________________________________ \n 1: Create Database		2: Create Table \n 3: Show Databases		4: Show Tables \n 5: Delete Databases		6: Delete Tables \n 7: Input Values		8: Auto \n 9: Exit \n option = "))

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
			d1.delete_db()

		# Delete Tables
		elif option==6:
			d1.delete_tb()

		# Input Values
		elif option==7:
			d1.input_values()

		# Auto
		elif option==8:
			d1.create_db()
			d1.create_tb()
			a = str(input("Do You Want to create Another tables(y/n?) : "))
			while a=="y":
				d1.create_tb()
				a = str(input("Do You Want to create Another tables(y/n?) : "))
			else:
				d1.input_values()
			
		# Exit
		elif option==9:
			break
		

if __name__ == "__main__":
	Main()


	

#created by Guardian-75.
#If You have any questions or advices,plz contact me.
#Contact mail : htetphyolin18@ucsmgy.edu.mm