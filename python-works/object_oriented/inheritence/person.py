class Person:

    name:str

    age:int

    gender:str

    def __init__(self,name,age,gender):

        self.name=name

        self.age=age

        self.gender=gender

    def display(self):

        print(f"name{self.name}age{self.age}gender of the person{self.gender}")

class Student(Person):

    roll=int

    course=str

    def __init__(self,name,age,gender,roll,course):
        
        super().__init__(name,age,gender)

        self.roll=roll

        self.course=course

    def display(self):

        super().display()

        print(f"rollno{self.roll}course{self.course}")

student_instance1=Student("manu",20,"male",2,"django")

student_instance1.display()