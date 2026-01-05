from mysql import connector

connection=connector.connect(
    host="localhost",
    user="root",
    password="Password@123",
    database="student_db",
    use_pure=True
)

cursor=connection.cursor()

query="select * from student"

cursor.execute(query)

records=cursor.fetchall()

for row in records:

    print(row)

cursor.close()

connection.close()
