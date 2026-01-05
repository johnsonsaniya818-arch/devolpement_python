class Rainbow:

    color:str

    number:int

    def __init__(self,color,number):

        self.color=color

        self.number=number

    def display(self):

        print(f"rainbow color is {self.color} the number of colors of a rainbow is {self.number}")

rainbow_instance1=Rainbow("green",7)

rainbow_instance1.display()