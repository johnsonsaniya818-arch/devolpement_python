from mysql import connector

connection=connector.connect(
    host="localhost",
    user="root",
    password="Password@123",
    database="student_db",
    use_pure=True

)

cursor=connection.cursor()

query="""
insert into user(name,email,phone) values(%s,%s,%s)
"""

data=[("manu","manu1@gmail.com","9678451245"),
      ("mani","mani@gmail.com","89754612100"),
      ("ravi","ravi@gmail.com","78965421300"),
      ("achu","achu@gmail.com","78956340231"),
      ]

cursor.executemany(query,data)

connection.commit()

print("query executed....")

cursor.close()

connection.close()

