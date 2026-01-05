class Animal:

    def __init__(self,name):

        self.name=name
   

    def sound(self):

        print(f"{self.sound}")

class Dog(Animal):

    def __init__(self, name):
        super().__init__(name)

    def sound(self):
        
        print(f"{self.name} bark")

class Cat(Animal):

    def __init__(self,name):
        super().__init__(name)

    def sound(self):
         
         print(f"{self.name} meow")

cat_instance1=Cat("cat")

cat_instance1.sound()

dog_instance1=Dog("dog")

dog_instance1.sound()
