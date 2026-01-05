class Mobile:

    name:str

    price:int

    features:str

    def __init__(self,name,price,features):

        self.name=name

        self.price=price

        self.features=features

    def display(self):

        print(f"mobile name {self.name} mobile price {self.price} mobile featues {self.features}")

mobile_instance1=Mobile("sumsung",15000,"easy to use")

mobile_instance1.display()

mobile_instance2=Mobile("poco",10000,"can take photos")

mobile_instance2.display()
        