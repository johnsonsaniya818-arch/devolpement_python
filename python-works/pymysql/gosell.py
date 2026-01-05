from mysql import connector

class Vehicles:

    def __init__(self):

        try:

            self.connection=connector.Connect(
                host="localhost",
                user="root",
                password="Password@123",
                database="gosell_db",
                use_pure=True
            )

            self.cursor=self.connection.cursor()
        
            print("db connection is ok...")

        except Exception as e:

            print(e)

    def add_vehicle(self,**kwargs):

        try:

            coloumns=""
            values=""

            for k,v in kwargs.items():
                coloumns+=k+","
                values+="%s"+","

            coloumns=coloumns.rstrip(",")
            
            values= values.rstrip(",")


            query=f"""
            insert into vehicle({coloumns})values({values})"""

            data=[v for k,v in kwargs.items()]

            self.cursor.execute(query,data)

            self.connection.commit()

            print("records inserted")

        except Exception as e:

            print(e)


    def list_vehicles(self):

        try:

            query="select * from vehicle"

            self.cursor.execute(query)

            records=self.cursor.fetchall()

            for row in records:

                print(row)
        except Exception as e:

            print(e)

    def select_one(self,id=None):
            
        try:

            query="select * from vehicle where id=%s"
            data=(id,)
            self.cursor.execute(query,data)

            records=self.cursor.fetchone()

            print(records)

        except Exception as e:

            print(e)

    def delete_vehicle(self,id=None):

        try:

            query="delete from vehicle where id=%s"
            data=(id,)
            self.cursor.execute(query,data)
            self.connection.commit()
            print("record deleted...")

        except Exception as e:

            print(e)

    def update_vehicle(self,id,**kwargs):

        place_holder=""

        for k,v in kwargs.items():

            place_holder+=k+"="+"%s"+","

        place_holder=place_holder.rstrip(",")

        query=f"update vehicle set {place_holder} where id={id}"

        data=[v for k,v in kwargs.items()]

        self.cursor.execute(query,data)

        self.connection.commit()

vehicle_insatance=Vehicles()

vehicle_insatance.add_vehicle(name="mahindra",price=100000,year='2000',fuel_type="petrol",comments="working condition",running_km=2000,owner_type="single",owner="arathy",location="Ernakulam")

vehicle_insatance.list_vehicles()

vehicle_insatance.select_one(7)

vehicle_insatance.delete_vehicle(3)

vehicle_insatance.list_vehicles()

vehicle_insatance.update_vehicle(7,price=600000)

vehicle_insatance.select_one(7)


            
