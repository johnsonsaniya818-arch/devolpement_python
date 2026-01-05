class Course:

    course_name:str

    def __init__(self,course_name):

        self.course_name=course_name

    def display(self):

        print(f"course name is {self.course_name}")

class Module(Course):

    module_name:str

    def __init__(self, course_name,module_name):
        
        super().__init__(course_name)

        self.module_name=module_name

    def display(self):
        
         super().display()

         print(f"module name {self.module_name}")

class Lesson(Module):

    lesson:str

    def __init__(self,lesson,course_name,module_name):

        super().__init__(course_name,module_name)

        self.lesson=lesson

    def display(self):
        
         super().display()

         print(f"lesson name {self.lesson}")

lessoninstance1=Lesson("inheritence","oops","python")

lessoninstance1.display()

        