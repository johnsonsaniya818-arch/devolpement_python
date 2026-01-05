class Person:

    name:str

    age:int

    gender:str

    def __init__(self,name,age,gender):

        self.name=name

        self.age=age

        self.gender=gender

    @property

    def get_gender(self):

        print(self.gender)

    @property

    def get_age(self):

        print(self.age)

person_instance1=Person("manu",12,"male")

print(person_instance1.name)

person_instance1.get_age#we dont use bracket for method calling because the function property decorator

person_instance1.get_gender