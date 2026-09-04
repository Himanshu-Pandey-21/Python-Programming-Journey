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
    query = "DELETE FROM empl WHERE Job = 'Clerk';"
    cur.execute(query)
    con.commit()

    print(cur.rowcount, "record(s) deleted successfully.")

except mysql.connector.Error as e:
    print("Error:", e)

finally:
    if con is not None and con.is_connected():
        if cur is not None:
            cur.close()
        con.close()
        print("Connection closed.")
