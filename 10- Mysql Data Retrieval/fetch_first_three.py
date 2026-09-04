import mysql.connector

con = None
cur = None

try:
    con = mysql.connector.connect(
        host="localhost",
        user="root",
        password=input("Enter MySQL password: "),
        database="employees"
    )

    cur = con.cursor()
    query = "SELECT * FROM empl LIMIT 3;"
    cur.execute(query)
    rows = cur.fetchall()

    print("First three records from emp table:\n")
    for row in rows:
        print(row)

except mysql.connector.Error as e:
    print("Error:", e)

finally:
    if con is not None and con.is_connected():
        if cur is not None:
            cur.close()
        con.close()
        print("Connection closed.")
