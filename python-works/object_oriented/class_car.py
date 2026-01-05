class Car:

    name:str

    brand:str

    price:int

    color:str

    def set_car(self,name,brand,price,color):

        self.name=name

        self.brand=brand

        self.price=price

        self.color=color

    def display(self):

        print(self.name,self.brand,self.price,self.color)

car_instance1=Car()

car_instance1.set_car("bmw","zusuki",1000000,"white")

car_instance1.display()

car_instance2=Car()

car_instance2.set_car("bens","honda",1000000,"black")

car_instance2.display()






