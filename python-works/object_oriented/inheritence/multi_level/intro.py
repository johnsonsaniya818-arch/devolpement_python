class Grandparent:

    def properties(self):

        print("50 acres of land")

class Parent(Grandparent):

    def vehicle(self):

        print("car")

class Child(Parent):

    def gadgets(self):

        print("phone,watch")

child_instance1=Child()

child_instance1.gadgets()

child_instance1.vehicle()#inherited from parent calss

child_instance1.properties()#inherited from grandparent