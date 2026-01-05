from mysql import connector

class employees:

    def __init__(self):

        try:
        
          self.connection=connector.connect(
                host="localhost",
                user="root",
                password="Password@123",
                database="employees_db",
                use_pure=True
            )
          
          self.cursor=self.connection.cursor()

          print("db connection is ok....")

        except Exception as e:

            print(e)

    def add_employee(self,**kwargs):
        
        try:

            column=""
            values=""
            for k,v in kwargs.items():

                column+=k+","
                values+="%s"+","
            column=column.rstrip(",")
            values=values.rstrip(",")

            query=f"""insert into employees({column})values({values})"""

            data=[v for k,v in kwargs.items()]

            self.cursor.execute(query,data)

            self.connection.commit()

            print("records inserted.....")

        except Exception as e:

            print(e)

    def list_employees(self):

        try:

            query=f"select * from employees"

            self.cursor.execute(query)

            records=self.cursor.fetchall()

            for row in records:

                print(row)

        except Exception as e:

            print(e)

    def select_one(self,id=None):

        try:

            query=f"select * from employees where id=%s"

            data=[id,]
            self.cursor.execute(query,data)
            records=self.cursor.fetchone()

            print(records)

        except Exception as e:

            print(e)

    def delete_employee(self,id=None):

        try:

            query="delete  from employees where id=%s" 

            data=(id,)

            self.cursor.execute(query,data)
            self.connection.commit()
            print("record deleted...")

        except Exception as e:

            print(e)

    def update_employees(self,id,**kwargs):
            
            try:

                placeholder=""

                for k,v in kwargs.items():

                    placeholder+=k+"="+"%s"+","

                placeholder=placeholder.rstrip(",")

                query=f"update employees set {placeholder} where id={id}"

                data=[v for k,v in kwargs.items()]

                self.cursor.execute(query,data)

                self.connection.commit()

            except Exception as e:

                print(e)

            









employees_insatnce=employees()

#employees_insatnce.add_employee(name="kannan",department="devolper",email="k0nann@gmail.com",phone=7732254103,salary="2000000")

#employees_insatnce.list_employees()

#employees_insatnce.select_one(3)

#employees_insatnce.delete_employee(4)

employees_insatnce.update_employees(5,salary=250000)

employees_insatnce.list_employees()


