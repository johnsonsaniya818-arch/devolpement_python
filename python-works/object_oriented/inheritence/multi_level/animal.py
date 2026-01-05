class Tiger:

    name=str

    sound=str

    color:str

    def __init__(self,sound,color,name):

        self.name=name

        self.sound=sound

        self.color=color

    def dispaly(self):

        print(f"The ancister animal {self.name} color is {self.color} sound of this{self.sound} ")

class LinedTiger(Tiger):

    hands:int

    legs:int

    def __init__(self,name,sound,color,hands,legs):

        super().__init__(name,sound,color)

        self.hands=hands

        self.legs=legs

    def dispaly(self):
        
        super().dispaly()
        
        print(f"hands {self.hands} legs {self.legs}")

class Cat(LinedTiger):

    sleep:int

    def __init__(self, name, sound, color, hands, legs,sleep):
        super().__init__(name, sound, color, hands, legs)

        self.sleep=sleep

    def dispaly(self):
        super().dispaly()

        print(f"sleep {self.sleep}")

cat_instance1=Cat("cat","meow","black",2,2,4)

cat_instance1.dispaly()
        