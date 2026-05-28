import mysql.connector

db_connect = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="employee"
)

print(db_connect)
if(db_connect):
    print("connection successful")
else:
    print("connection failed")

def getAllEmployeeData():
    cursor = db_connect.cursor()
    query = "SELECT * FROM employee"
    cursor.execute(query)
    result = cursor.fetchall()  # Fetch the actual data
    for row in result:
        print(row)
    cursor.close()
    db_connect.close()
    # Do NOT close db_connect here

getAllEmployeeData()   
