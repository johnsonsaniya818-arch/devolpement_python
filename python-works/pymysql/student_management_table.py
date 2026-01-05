from mysql import connector

class Student:

    def __init__(self):

        try:

            self.connection=connector.Connect(
                host="localhost",
                user="root",
                password="Password@123",
                database="student_management_db",
                use_pure=True
            )

            self.cursor=self.connection.cursor()
        
            print("db connection is ok...")

        except Exception as e:

            print(e)

    def add_student(self,**kwargs):

        try:

            coloumns=""
            values=""

            for k,v in kwargs.items():
                coloumns+=k+","
                values+="%s"+","

            coloumns=coloumns.rstrip(",")
            
            values= values.rstrip(",")


            query=f"""
            insert into student({coloumns})values({values})"""

            data=[v for k,v in kwargs.items()]

            self.cursor.execute(query,data)

            self.connection.commit()

            print("records inserted")

        except Exception as e:

            print(e)


    def list_student(self):

        try:

            query="select * from student"

            self.cursor.execute(query)

            records=self.cursor.fetchall()

            for row in records:

                print(row)
        except Exception as e:

            print(e)

    def select_one(self,id=None):
            
        try:

            query="select * from student where id=%s"
            data=(id,)
            self.cursor.execute(query,data)

            records=self.cursor.fetchone()

            print(records)

        except Exception as e:

            print(e)

    def delete_student(self,id=None):

        try:

            query="delete from student where id=%s"
            data=(id,)
            self.cursor.execute(query,data)
            self.connection.commit()
            print("record deleted...")

        except Exception as e:

            print(e)

    def update_student(self,id,**kwargs):

        place_holder=""

        for k,v in kwargs.items():

            place_holder+=k+"="+"%s"+","

        place_holder=place_holder.rstrip(",")

        query=f"update student set {place_holder} where id={id}"

        data=[v for k,v in kwargs.items()]

        self.cursor.execute(query,data)

        self.connection.commit()

student_insatance=Student()

#student_insatance.add_student(name="chimmu",department="Mba",fee=500000)

#student_insatance.list_student()

#student_insatance.select_one(2)

#student_insatance.delete_student(3)

#student_insatance.list_student()

student_insatance.update_student(5,fee=600000)

student_insatance.select_one(5)


            
