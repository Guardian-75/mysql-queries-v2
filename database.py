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

# option = int(input(" [1] Create database\n [2] Create table\n input : "))

# if option==1:
# 	create_db()
	
# elif option==2:
# 	create_tb()

import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="guardian",
  database="aa"
)

mycursor = mydb.cursor()

sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
val = [
  ('Peter', 'Lowstreet 4'),
  ('Amy', 'Apple st 652'),
  ('Hannah', 'Mountain 21'),
  ('Michael', 'Valley 345'),
  ('Sandy', 'Ocean blvd 2'),
  ('Betty', 'Green Grass 1'),
  ('Richard', 'Sky st 331'),
  ('Susan', 'One way 98'),
  ('Vicky', 'Yellow Garden 2'),
  ('Ben', 'Park Lane 38'),
  ('William', 'Central st 954'),
  ('Chuck', 'Main Road 989'),
  ('Viola', 'Sideway 1633')
]

mycursor.executemany(sql, val)

mydb.commit()

print(mycursor.rowcount, "was inserted.")