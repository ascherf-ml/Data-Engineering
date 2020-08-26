# -*- coding: utf-8 -*-
"""
Spyder Editor

Dies ist eine temporäre Skriptdatei.
"""


# import postgreSQL adapter for the Python
import psycopg2


# Connect to a server
conn = psycopg2.connect(host='127.0.0.1',
                        dbname='postgres',
                        user='postgres',
                        password='bladeoi12')

# set autocommit to true in order to avoid blocking transactions by transactions that are not
# finished yet
conn.set_session(autocommit=True)

# create a cursor to execute queries
cur = conn.cursor()




# =============================================================================
# Creating a database
# =============================================================================
cur.execute('create database udacity')

# closing a connection
conn.close()

# connect to Database
conn = psycopg2.connect(dbname='udacity', 
                        user='postgres',
                        password='bladeoi12')
# create a cursor to execute queries
cur = conn.cursor()

# =============================================================================
# Create a table
# =============================================================================

try: 
    cur.execute("CREATE TABLE IF NOT EXISTS transactions2 \
    (transaction_id int, customer_name varchar, cashier_id int, year int)")
except psycopg2.Error as e: 
    print("Error: Issue creating table")
    print (e)

# calling the cursor and executing a query
# there is no need for ALL CAPS, just for readability
# varchar is a string
# int is a int variable
# text is a list



# =============================================================================
# Inserting rows
# =============================================================================

    
try: 
    cur.execute("INSERT INTO transactions2 (transaction_id, customer_name, cashier_id, year) \
                 VALUES (%s, %s, %s, %s)", \
                 (1, 'Amanda', 1, 2000))
except psycopg2.Error as e: 
    print("Error: Inserting Rows")
    print (e)
    
try: 
    cur.execute("INSERT INTO transactions2 (transaction_id, customer_name, cashier_id, year) \
                 VALUES (%s, %s, %s, %s)", \
                 (2, 'Toby', 1, 2000))
except psycopg2.Error as e: 
    print("Error: Inserting Rows")
    print (e)
    
try: 
    cur.execute("INSERT INTO transactions2 (transaction_id, customer_name, cashier_id, year) \
                 VALUES (%s, %s, %s, %s)", \
                 (3, 'Max', 2, 2018))
except psycopg2.Error as e: 
    print("Error: Inserting Rows")
    print (e)
    


# =============================================================================
# Getting values
# =============================================================================

try: 
    cur.execute("SELECT * FROM transactions2")
except psycopg2.Error as e: 
    print("Error: select *")
    print (e)

row = cur.fetchone()
while row:
   print(row)
   row = cur.fetchone()

# =============================================================================
# 1NF
# First Normal Form 
# =============================================================================
'Rows are split in a way, that there is only one information per cell'

try: 
    cur.execute("CREATE TABLE IF NOT EXISTS music_store2\
    (transaction_id int, customer_name varchar, cashier_name varchar, year int, purchases varchar);")
except psycopg2.Error as e: 
    print("Error: Issue creating table")
    print (e)
    
try: 
    cur.execute("INSERT INTO music_store2\
    (transaction_id, customer_name, cashier_name, year, purchases) \
                 VALUES (%s, %s, %s, %s, %s)", \
                 (1, 'Amanda', 'Sam', 2000, 'Rubber Soul'))
except psycopg2.Error as e: 
    print("Error: Inserting Rows")
    print (e)

try: 
    cur.execute("INSERT INTO music_store2 (transaction_id, customer_name, cashier_name, year, purchases) \
                 VALUES (%s, %s, %s, %s, %s)", \
                 (1, 'Amanda', 'Sam', 2000, 'Let it Be'))
except psycopg2.Error as e: 
    print("Error: Inserting Rows")
    print (e)
    
try: 
    cur.execute("INSERT INTO music_store2 (transaction_id, customer_name, cashier_name, year, purchases) \
                 VALUES (%s, %s, %s, %s, %s)", \
                 (2, 'Toby', 'Sam', 2000, 'My Generation'))
except psycopg2.Error as e: 
    print("Error: Inserting Rows")
    print (e)
    
try: 
    cur.execute("INSERT INTO music_store2 (transaction_id, customer_name, cashier_name, year, purchases) \
                 VALUES (%s, %s, %s, %s, %s)", \
                 (3, 'Max', 'Bob', 2018, 'Meet the Beatles'))
except psycopg2.Error as e: 
    print("Error: Inserting Rows")
    print (e)
    
try: 
    cur.execute("INSERT INTO music_store2 (transaction_id, customer_name, cashier_name, year, purchases) \
                 VALUES (%s, %s, %s, %s, %s)", \
                 (3, 'Max', 'Bob', 2018,'Help!'))
except psycopg2.Error as e: 
    print("Error: Inserting Rows")
    print (e)
    
try: 
    cur.execute("SELECT * FROM music_store2;")
except psycopg2.Error as e: 
    print("Error: select *")
    print (e)

row = cur.fetchone()
while row:
   print(row)
   row = cur.fetchone()


# =============================================================================
# 2NF
# Second Normal Form
# =============================================================================
'The data is split along the transaction_id into two tables'


try: 
    cur.execute("CREATE TABLE IF NOT EXISTS transactions\
    (transaction_id int, customer_name varchar, cashier_name varchar, year int);")
except psycopg2.Error as e: 
    print("Error: Issue creating table")
    print (e)

try: 
    cur.execute("CREATE TABLE IF NOT EXISTS albums_sold\
    (transaction_id int,purchase_number int, purchases varchar);")
except psycopg2.Error as e: 
    print("Error: Issue creating table")
    print (e)
    
try: 
    cur.execute("INSERT INTO transactions (transaction_id, customer_name, cashier_name, year) \
                 VALUES (%s, %s, %s, %s)", \
                 (1, 'Amanda', 'Sam', 2000,))
except psycopg2.Error as e: 
    print("Error: Inserting Rows")
    print (e)

try: 
    cur.execute("INSERT INTO transactions (transaction_id, customer_name, cashier_name, year) \
                 VALUES (%s, %s, %s, %s)", \
                 (2, 'Toby', 'Sam', 2000))
except psycopg2.Error as e: 
    print("Error: Inserting Rows")
    print (e)
    
try: 
    cur.execute("INSERT INTO transactions (transaction_id, customer_name, cashier_name, year) \
                 VALUES (%s, %s, %s, %s)", \
                 (3, 'Max', 'Bob', 2018))
except psycopg2.Error as e: 
    print("Error: Inserting Rows")
    print (e)
    
try: 
    cur.execute("INSERT INTO albums_sold (transaction_id, purchase_number, purchases) \
                 VALUES (%s, %s, %s)", \
                 (1,1,'Rubber Soul'))
except psycopg2.Error as e: 
    print("Error: Inserting Rows")
    print (e)

try: 
    cur.execute("INSERT INTO albums_sold (transaction_id, purchase_number, purchases) \
                 VALUES (%s, %s, %s)", \
                 (1,2,'Let it Be'))
except psycopg2.Error as e: 
    print("Error: Inserting Rows")
    print (e)
    
try: 
    cur.execute("INSERT INTO albums_sold (transaction_id, purchase_number, purchases) \
                 VALUES (%s, %s, %s)", \
                 (2,1,'My Generation'))
except psycopg2.Error as e: 
    print("Error: Inserting Rows")
    print (e)
    
try: 
    cur.execute("INSERT INTO albums_sold (transaction_id, purchase_number, purchases) \
                 VALUES (%s, %s, %s)", \
                 (3,1,'Meet the Beatles' ))
except psycopg2.Error as e: 
    print("Error: Inserting Rows")
    print (e)

try: 
    cur.execute("INSERT INTO albums_sold (transaction_id, purchase_number, purchases) \
                 VALUES (%s, %s, %s)", \
                 (3,2, 'Help!'))
except psycopg2.Error as e: 
    print("Error: Inserting Rows")
    print (e)

print("Table: transactions\n")
try: 
    cur.execute("SELECT * FROM transactions;")
except psycopg2.Error as e: 
    print("Error: select *")
    print (e)

row = cur.fetchone()
while row:
   print(row)
   row = cur.fetchone()

print("\nTable: albums_sold\n")
try: 
    cur.execute("SELECT * FROM albums_sold;")
except psycopg2.Error as e: 
    print("Error: select *")
    print (e)
row = cur.fetchone()
while row:
   print(row)
   row = cur.fetchone()

# =============================================================================
# Joining tables
# =============================================================================

# Joining the transactions and album_sold tables

try: 
    cur.execute("SELECT * FROM transactions JOIN albums_sold ON transactions.transaction_id = albums_sold.transaction_id ;")
except psycopg2.Error as e: 
    print("Error: select *")
    print (e)

row = cur.fetchone()
while row:
   print(row)
   row = cur.fetchone()


# =============================================================================
# 3NF
# Third Normal Form
# =============================================================================
'The data is split along the transaction_id into two tables'

try: 
    cur.execute("CREATE TABLE IF NOT EXISTS transactions2\
    (transaction_id int, customer_name varchar, cashier_number int, year int);")
except psycopg2.Error as e: 
    print("Error: Issue creating table")
    print (e)

try: 
    cur.execute("CREATE TABLE IF NOT EXISTS employees (cashier_number int, cashier_name varchar);")
except psycopg2.Error as e: 
    print("Error: Issue creating table")
    print (e)

try: 
    cur.execute("INSERT INTO transactions2 (transaction_id, customer_name, cashier_number, year) \
                 VALUES (%s, %s, %s, %s)", \
                 (1, 'Amanda', 1, 2000))
except psycopg2.Error as e: 
    print("Error: Inserting Rows")
    print (e)

try: 
    cur.execute("INSERT INTO transactions2 (transaction_id, customer_name, cashier_number, year) \
                 VALUES (%s, %s, %s, %s)", \
                 (2, 'Toby', 1, 2000))
except psycopg2.Error as e: 
    print("Error: Inserting Rows")
    print (e)
    
try: 
    cur.execute("INSERT INTO transactions2 (transaction_id, customer_name, cashier_number, year) \
                 VALUES (%s, %s, %s, %s)", \
                 (3, 'Max', 2, 2018))
except psycopg2.Error as e: 
    print("Error: Inserting Rows")
    print (e)

try: 
    cur.execute("INSERT INTO employees (cashier_number, cashier_name) \
                 VALUES (%s, %s)", \
                 (1, 'Sam'))
except psycopg2.Error as e: 
    print("Error: Inserting Rows")
    print (e)

try: 
    cur.execute("INSERT INTO employees (cashier_number, cashier_name) \
                 VALUES (%s, %s)", \
                 (2, 'Bob'))
except psycopg2.Error as e: 
    print("Error: Inserting Rows")
    print (e)    

print("Table: transactions2\n")
try: 
    cur.execute("SELECT * FROM transactions2;")
except psycopg2.Error as e: 
    print("Error: select *")
    print (e)

row = cur.fetchone()
while row:
   print(row)
   row = cur.fetchone()

print("\nTable: albums_sold\n")
try: 
    cur.execute("SELECT * FROM albums_sold;")
except psycopg2.Error as e: 
    print("Error: select *")
    print (e)

row = cur.fetchone()
while row:
   print(row)
   row = cur.fetchone()

print("\nTable: employees\n")
try: 
    cur.execute("SELECT * FROM employees;")
except psycopg2.Error as e: 
    print("Error: select *")
    print (e)

row = cur.fetchone()
while row:
   print(row)
   row = cur.fetchone()
   
# =============================================================================
# Joining 3 Tables
# =============================================================================

try: 
    cur.execute("SELECT * FROM (transactions2 JOIN albums_sold ON \
                               transactions2.transaction_id = albums_sold.transaction_id) JOIN \
                               employees ON transactions2.cashier_number=employees.cashier_number;")
except psycopg2.Error as e: 
    print("Error: select *")
    print (e)

row = cur.fetchone()
while row:
   print(row)
   row = cur.fetchone()



# =============================================================================
# Denormalization
# =============================================================================

try: 
    cur.execute("CREATE TABLE IF NOT EXISTS transactions2 \
    (transaction_id int, customer_name varchar, cashier_id int, year int)")
except psycopg2.Error as e: 
    print("Error: Issue creating table")
    print (e)

try: 
    cur.execute("CREATE TABLE IF NOT EXISTS albums_sold \
    (transaction_id int, album_id int, album_name varchar)")
except psycopg2.Error as e: 
    print("Error: Issue creating table")
    print (e)

try: 
    cur.execute("CREATE TABLE IF NOT EXISTS employees \
    (employee_id int, employee_name varchar)")
except psycopg2.Error as e: 
    print("Error: Issue creating table")
    print (e)

try: 
    cur.execute("CREATE TABLE IF NOT EXISTS sales \
    (transaction_id int, amount_spend int)")
except psycopg2.Error as e: 
    print("Error: Issue creating table")
    print (e)

      
# Insert data into the tables    
       
try: 
    cur.execute("INSERT INTO transactions2 (transaction_id, customer_name, cashier_id, year) \
                 VALUES (%s, %s, %s, %s)", \
                 (1, 'Amanda', 1, 2000))
except psycopg2.Error as e: 
    print("Error: Inserting Rows")
    print (e)
    
try: 
    cur.execute("INSERT INTO transactions2 (transaction_id, customer_name, cashier_id, year) \
                 VALUES (%s, %s, %s, %s)", \
                 (2, 'Toby', 1, 2000))
except psycopg2.Error as e: 
    print("Error: Inserting Rows")
    print (e)
    
try: 
    cur.execute("INSERT INTO transactions2 (transaction_id, customer_name, cashier_id, year) \
                 VALUES (%s, %s, %s, %s)", \
                 (3, 'Max', 2, 2018))
except psycopg2.Error as e: 
    print("Error: Inserting Rows")
    print (e)
    
try: 
    cur.execute("INSERT INTO albums_sold (album_id, transaction_id, album_name) \
                 VALUES (%s, %s, %s)", \
                 (1, 1, "Rubber Soul"))
except psycopg2.Error as e: 
    print("Error: Inserting Rows")
    print (e)

try: 
    cur.execute("INSERT INTO albums_sold (album_id, transaction_id, album_name) \
                 VALUES (%s, %s, %s)", \
                 (2, 1, "Let It Be"))
except psycopg2.Error as e: 
    print("Error: Inserting Rows")
    print (e)
    
try: 
    cur.execute("INSERT INTO albums_sold (album_id, transaction_id, album_name) \
                 VALUES (%s, %s, %s)", \
                 (3, 2, "My Generation"))
except psycopg2.Error as e: 
    print("Error: Inserting Rows")
    print (e)
    
try: 
    cur.execute("INSERT INTO albums_sold (album_id, transaction_id, album_name) \
                 VALUES (%s, %s, %s)", \
                 (4, 3, "Meet the Beatles"))
except psycopg2.Error as e: 
    print("Error: Inserting Rows")
    print (e)

try: 
    cur.execute("INSERT INTO albums_sold (album_id, transaction_id, album_name) \
                 VALUES (%s, %s, %s)", \
                 (5, 3, "Help!"))
except psycopg2.Error as e: 
    print("Error: Inserting Rows")
    print (e)

try: 
    cur.execute("INSERT INTO employees (employee_id, employee_name) \
                 VALUES (%s, %s)", \
                 (1, "Sam"))
except psycopg2.Error as e: 
    print("Error: Inserting Rows")
    print (e)

try: 
    cur.execute("INSERT INTO employees (employee_id, employee_name) \
                 VALUES (%s, %s)", \
                 (2, "Bob"))
except psycopg2.Error as e: 
    print("Error: Inserting Rows")
    print (e)    
    
try: 
    cur.execute("INSERT INTO sales (transaction_id, amount_spend) \
                 VALUES (%s, %s)", \
                 (1, 40))
except psycopg2.Error as e: 
    print("Error: Inserting Rows")
    print (e)    
    
try: 
    cur.execute("INSERT INTO sales (transaction_id, amount_spend) \
                 VALUES (%s, %s)", \
                 (2, 19))
except psycopg2.Error as e: 
    print("Error: Inserting Rows")
    print (e) 

try: 
    cur.execute("INSERT INTO sales (transaction_id, amount_spend) \
                 VALUES (%s, %s)", \
                 (3, 45))
except psycopg2.Error as e: 
    print("Error: Inserting Rows")
    print (e) 

# Print tables to see, if everything is inserted

print("Table: transactions2\n")
try: 
    cur.execute("SELECT * FROM transactions2;")
except psycopg2.Error as e: 
    print("Error: select *")
    print (e)

row = cur.fetchone()
while row:
   print(row)
   row = cur.fetchone()

print("\nTable: albums_sold\n")
try: 
    cur.execute("SELECT * FROM albums_sold;")
except psycopg2.Error as e: 
    print("Error: select *")
    print (e)

row = cur.fetchone()
while row:
   print(row)
   row = cur.fetchone()

print("\nTable: employees\n")
try: 
    cur.execute("SELECT * FROM employees;")
except psycopg2.Error as e: 
    print("Error: select *")
    print (e)

row = cur.fetchone()
while row:
   print(row)
   row = cur.fetchone()
    
print("\nTable: sales\n")
try: 
    cur.execute("SELECT * FROM sales;")
except psycopg2.Error as e: 
    print("Error: select *")
    print (e)

row = cur.fetchone()
while row:
   print(row)
   row = cur.fetchone()
   
# =============================================================================
# Joining tables
# =============================================================================

# Joining the 4 tables with a 3 way join

   
try: 
    cur.execute("SELECT transactions2.transaction_id, transactions2.customer_name,\
    employees.employee_name, transactions2.year, albums_sold.album_name, sales.amount_spend\
    FROM ((transactions2 JOIN albums_sold ON transactions2.transaction_id = albums_sold.transaction_id)\
    JOIN\
    employees ON transactions2.cashier_id=employees.employee_id)\
    JOIN\
    sales on transactions2.transaction_id=sales.transaction_id;")
    
    
except psycopg2.Error as e: 
    print("Error: select *")
    print (e)

row = cur.fetchone()
while row:
   print(row)
   row = cur.fetchone()
   

# Because a 3 way JOIN is heavy on the calculations, a solution might be to dublicate tables for specific queries

try: 
    cur.execute("CREATE TABLE IF NOT EXISTS cashier_sales (transaction_id int, cashier_name varchar, \
                                                           cashier_id int, amount_spent int);")
except psycopg2.Error as e: 
    print("Error: Issue creating table")
    print (e)


#Insert into all tables 
    
try: 
    cur.execute("INSERT INTO cashier_sales (transaction_id, cashier_name, cashier_id, amount_spent) \
                 VALUES (%s, %s, %s, %s)", \
                 (1, "Sam", 1, 40 ))
except psycopg2.Error as e: 
    print("Error: Inserting Rows")
    print (e)

try: 
    cur.execute("INSERT INTO cashier_sales (transaction_id, cashier_name, cashier_id, amount_spent) \
                 VALUES (%s, %s, %s, %s)", \
                 (2, "Sam", 1, 19 ))
except psycopg2.Error as e: 
    print("Error: Inserting Rows")
    print (e)

try: 
    cur.execute("INSERT INTO cashier_sales (transaction_id, cashier_name, cashier_id, amount_spent) \
                 VALUES (%s, %s, %s, %s)", \
                 (3, "Max", 2, 45))
except psycopg2.Error as e: 
    print("Error: Inserting Rows")
    print (e)
    
# List the sum of sales for a cashier

try: 
    cur.execute("select cashier_name, SUM(amount_spent) FROM cashier_sales GROUP BY cashier_name;")
        
except psycopg2.Error as e: 
    print("Error: select *")
    print (e)

row = cur.fetchone()
while row:
   print(row)
   row = cur.fetchone()

# =============================================================================
# Deleting a table
# =============================================================================
try: 
    cur.execute("DROP table transactions2")
except psycopg2.Error as e: 
    print("Error: Dropping table")
    print (e)
try: 
    cur.execute("DROP table albums_sold")
except psycopg2.Error as e: 
    print("Error: Dropping table")
    print (e)
try: 
    cur.execute("DROP table employees")
except psycopg2.Error as e: 
    print("Error: Dropping table")
    print (e)
try: 
    cur.execute("DROP table sales")
except psycopg2.Error as e: 
    print("Error: Dropping table")
    print (e)
    
try: 
    cur.execute("DROP table music_store")
except psycopg2.Error as e: 
    print("Error: Dropping table")
    print (e)
try: 
    cur.execute("DROP table music_store2")
except psycopg2.Error as e: 
    print("Error: Dropping table")
    print (e)
try: 
    cur.execute("DROP table albums_sold")
except psycopg2.Error as e: 
    print("Error: Dropping table")
    print (e)
try: 
    cur.execute("DROP table employees")
except psycopg2.Error as e: 
    print("Error: Dropping table")
    print (e)
try: 
    cur.execute("DROP table transactions")
except psycopg2.Error as e: 
    print("Error: Dropping table")
    print (e)
try: 
    cur.execute("DROP table transactions2")
except psycopg2.Error as e: 
    print("Error: Dropping table")
    print (e)


# Closing the cursor and the connection to the server
cur.close()
conn.close()