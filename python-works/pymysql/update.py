from mysql import connector

connection=connector.connect(
    host="localhost",
    user="root",
    password="Password@123",
    database="student_db",
    use_pure=True
)

cursor=connection.cursor()

query="update user set name= %s,password=%s where id=%s" 
""

data=("aswathy","aswathy@gmail.com",9)

cursor.execute(query,data)

connection.commit()


print("record updated")

cursor.close()

connection.close()

