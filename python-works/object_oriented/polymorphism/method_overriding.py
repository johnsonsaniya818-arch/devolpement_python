class Vehicle:

    def __init__(self,brand,title):

        self.brand=brand

        self.title=title

    def move(self):

        print(f"{self.title} is moving")

class Car(Vehicle):

    def __init__(self,brand,title):

        super().__init__(brand,title)

class Ship(Vehicle):

    def __init__(self, brand, title):
        super().__init__(brand, title)

    def move(self):

            print(f"{self.title} is saling")

car_instance1=Car("toyota","rolce roice")

car_instance1.move()

ship_instance1=Ship("mitsu","titanic")

ship_instance1.move()