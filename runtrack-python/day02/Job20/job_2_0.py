class Person:
    # Instance attribute
    def __init__(self, name, first_name):
        self.name = name
        self.first_name = first_name

    def SePresenter(self):
        print("My name is", self.name )
        print("My first name is", self.first_name )
    
    def accessorN(self):
        return self.name 
    
    def accessorFN(self):
        return self.first_name 
    
    def mutatorN(self,new_name):
        self.name = new_name

    def mutatorFN(self,new_first_name):
        self.first_name = new_first_name

