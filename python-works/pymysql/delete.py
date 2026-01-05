from mysql import connector

connection=connector.connect(
    host="localhost",
    user="root",
    password="Password@123",
    database="student_db",
    use_pure=True
)

cursor=connection.cursor()

query="delete from students where id=%s"

data=(6,)

cursor.execute(query,data)
connection.commit()

print("record deleted")

