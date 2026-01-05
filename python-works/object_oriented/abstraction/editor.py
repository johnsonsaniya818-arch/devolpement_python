from abc import ABC 

from abc import abstractmethod

class Editor(ABC):

    @abstractmethod

    def create_module_and_packages(self):

        pass

    @abstractmethod

    def edit(self):

        pass

    @abstractmethod

    def excute(self):

        pass

    @abstractmethod

    def debug(self):

        pass

class VsCode(Editor):

    def create_module_and_packages(self):
        
        print("creating vscode packages and modules")

    def edit(self):

        print("eding in vscode")

    def excute(self):

        print("excuting in vscode")

    def debug(self):
        
        print("debugging in vscode")

vscode_instance=VsCode()

vscode_instance.create_module_and_packages()

vscode_instance.edit()

vscode_instance.excute()

vscode_instance.debug()