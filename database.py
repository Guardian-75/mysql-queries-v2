def create_db():
	import mysql.connector

	mydb = mysql.connector.connect(
		host="localhost",
		user="root",
		password="guardian"
	)

	db_name = str(input("Enter Your Database Name : "))
	creat_db_query = "CREATE DATABASE " + db_name

	mycursor = mydb.cursor()
	mycursor.execute(creat_db_query)
	mycursor.execute("SHOW DATABASES")

	for x in mycursor:
		print(x) 

	mycursor.close()
	mydb.close()


def create_tb():
	db_name = str(input("Enter Your Database Name : "))

	import mysql.connector

	mydb = mysql.connector.connect(
		host="localhost",
		user="root",
		password="guardian",
		database=db_name,
	)

	mycursor = mydb.cursor()
	mycursor.execute("CREATE TABLE customers (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), address VARCHAR(255))")
	mycursor.execute("SHOW TABLES")

	for x in mycursor:
		print(x)

	mycursor.close()
	mydb.close()

option = int(input(" [1] Create database\n [2] Create table\n input : "))

if option==1:
	create_db()
	
elif option==2:
	create_tb()
