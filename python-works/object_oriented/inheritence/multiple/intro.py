class Father:

    def cooking_skill(self):

        print("cooking")

class Mother:

    def dance_skill(self):

        print("dancing")

class Child(Father,Mother):

    def run_skill(self):

        print("running") 

child_instance1=Child()

child_instance1.cooking_skill()

child_instance1.dance_skill()

child_instance1.run_skill()