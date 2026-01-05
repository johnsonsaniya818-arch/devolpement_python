class Framework:

    name:str

    language:str

    architecture:str

    def set_framewrk(self,name,language,architecture):

        self.name=name

        self.language=language

        self.architecture=architecture

    def display(self):

        print(self.name,self.language,self.architecture)

asp=Framework()

django=Framework()

asp.set_framewrk("asp.net","c#","mvc")

django.set_framewrk("django","python","mvt")


asp.display()

django.display()
