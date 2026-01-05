class Employee:

    id:int

    department:str

    salary:int

    def __init__(self,id,department,salary):

        self.id=id

        self.department=department

        self.salary=salary

    def display(self):

        print(f"id {self.id} department {self.department} salary {self.salary}")

class Devolper(Employee):

    programming_language:str

    frame_work:str

    def __init__(self,id,department,salary,programmingl,framework):

        super().__init__(id,department,salary)

        self.programmingl=programmingl

        self.framework=framework

    def display(self):
         
         super().display()

         print(f"programming language {self.programmingl} framework {self.framework}")
         

devolper_instance1=Devolper(12,"devolper",25000,"python","django")

devolper_instance1.display()

        