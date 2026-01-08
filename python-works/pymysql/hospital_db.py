from mysql import connector

class Hospital:

    def __init__(self):
            
        try:
            self.connection=connector.connect(
            host="localhost",
            user="root",
            password="Password@123",
            database="hospital_db",
            use_pure=True

            )

            self.cursor=self.connection.cursor()

            print("dabase connection is ok....")

        except Exception as e:
                 
                 print(e)

    def POST(self,**kwargs):
         
        try:
         
            coloumn=""

            values=""

            for k,v in kwargs.items():
                
                coloumn+=k+","

                values+="%s"+","

            coloumn=coloumn.rstrip(",")

            values=values.rstrip(",")

            query=f"""
            
            insert into hospital({coloumn})values({values})"""

            data=[v for k,v in kwargs.items()]

            self.cursor.execute(query,data)

            self.connection.commit()

            print("inserted records....")

        except Exception as e:

            print(e)
    
    def GET(self,):
         
        try:
         
            query="select * from hospital"

            self.cursor.execute(query)

            records=self.cursor.fetchall()

            for row in records:

                print(row)

        except Exception as e:
             
             print(e)

    def GET(self,id=None):
         
         query="select * from hospital where id=%s"

         data=(id,)

         self.cursor.execute(query,data)

         records=self.cursor.fetchone()

         print(records)

    def DELETE(self,id=None):
         
         query="delete from hospital where id=%s"

         data=(id,)

         self.cursor.execute(query,data)

         self.connection.commit()

         print("record is deleted")

    def PUT(self,id,**kwargs):
        
        try:

            place_holder=""

            for k,v in kwargs.items():

                place_holder+=k+"="+"%s"+","

            place_holder=place_holder.rstrip(",")

            query=f"update hospital set {place_holder} where id={id}"

            data=[v for k,v in kwargs.items()]

            self.cursor.execute(query,data)

            self.connection.commit()

        except Exception as e:
             
             print(e)


         



        


hospital_instance=Hospital()

hospital_instance.POST(patient_name="kunju",patient_age=12,disease="heart disease",phone=647457812)

hospital_instance.GET()

hospital_instance.GET(7)

hospital_instance.DELETE(16)

hospital_instance.PUT(7,patient_age=22)

hospital_instance.GET()


