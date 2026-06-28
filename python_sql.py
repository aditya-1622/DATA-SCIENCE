# Connect Python to a SQL database
# Execute SQL queries from Python
# Read query results into Python
# Perform CRUD operations (Create, Read, Update, Delete)
# Understand what cursors are
# Understand why libraries like SQLAlchemy exist


# Why do we need Python + SQL Integration?
# Python → Variables, list, dict, dataframes
# SQL    → Data Stored inside databases..



# In a real project, there's a possibility that both are needed!
# Customer data is stored in SQL  → Python fetches the data  → Pandas analysis the data
# → EDA → ML Model does prediction → Store results back to SQL..



# Without integration : Python, SQL are 2 different worlds!
# With integration   : Database ↔ Python..


# Architecture to connect python with sql is : 
# Python  → MySQLConnector → MySQLServer → SQL WB..



import mysql.connector 
conn = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "AdityaPalak@1622",
    database = "aditya"
)
print("Connection established successfully!")


# host - where database server is runnning
# user - database username
# password - authentication
# database - which db to connect with


# What is a cursor?
# A cursor is an object : 
    # i. Sends SQL queries 
    # ii. Received SQL results


# Python - Cursor - Database

# You = Python
# Waiter = Cursor
# Kitchen = Database

# Create a cursor object
cursor = conn.cursor()

# Execute SQL query using cursor

# execute() : used to send SQL commands!
cursor.execute("SELECT * FROM employees")

# Fetch all results
# fetchall() : Return all rows!
results = cursor.fetchall()
print(results)


type(results) # list [] of tuples()!


for row in results:
    print(row)


cursor.execute(
    "SELECT * FROM employees"
)

# fetchone() : Return only one row!
rw_1 = cursor.fetchone()
print(rw_1)
# Check this?



# Convert the results to a Pandas df

import pandas as pd
# cursor.execute(
#     "SELECT * FROM EMPLOYEE"
# )

# rows = cursor.fetchall()
# rows

cursor.description


columns = [
    col[0]
    for col in cursor.description
]

columns

df = pd.DataFrame(
    results, columns=columns
)

print(df)



# Part 2 : 
# CRUD operations : Create, Read, Update, Delete

import mysql.connector
conn = mysql.connector.connect(
    host = "localhost", # if using google colab : server ip/domain (host="127.0.0.1")
    user = "root",
    password = "AdityaPalak@1622", # workbench password # enter your own password!
    database = "aditya",
    use_pure = True
)

cursor = conn.cursor()


#cursor.execute("""
#INSERT INTO employees
#(employee_id, employee_name, department, city, salary)
#VALUES
#(3,'Adi','Police','Mumbai', 50000)
#""")

# Is this row already inserted in the table or not?
conn.commit() # save button!

cursor.execute(
    "SELECT * FROM employees"
)

results = cursor.fetchall()

print(results)


# Update, Delete command on the same table and verify!
cursor.execute("""
UPDATE employees
SET salary=90000
WHERE department='HR'
""")

conn.commit()


cursor.execute(
    "SELECT * FROM employees"
)

results = cursor.fetchall()

print(results)


cursor.execute("""
DELETE FROM employees
WHERE department='Police'
""")

conn.commit()

cursor.execute(
    "SELECT * FROM employees"
)

results= cursor.fetchall()
print(results)


cursor.close()
conn.close()

# from sqlalchemy import create_engine

# engine = create_engine(
#     "mysql+pymysql://root:root123@localhost/company_db"
# )

# import pandas as pd

# df = pd.read_sql(
#     "SELECT * FROM employees",
#     engine
# )

# print(df)

# mysql          -> Database type
# pymysql        -> Driver
# root           -> Username
# password       -> Password
# localhost      -> Host
# company_db     -> Database name

# Example 1 : Local SQL : 
# engine = create_engine(
#     "mysql+pymysql://root:root123@localhost/company_db"
# )

# Example 2 : PostgreSQL : 
# engine = create_engine(
#     "postgresql://postgres:admin123@localhost/company_db"
# )

# mysql+pymysql://root:root123@localhost/company_db
# │      │         │       │          │
# DB   Driver    User   Password    Database