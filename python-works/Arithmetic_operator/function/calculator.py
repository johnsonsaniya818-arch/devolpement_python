class Calculator:

    def add(self,*args):

        print(sum(args))

calculator_instance1=Calculator()

calculator_instance1.add(20,30)

calculator_instance1.add(100,200,300)

calculator_instance1.add(20,30,50,20)