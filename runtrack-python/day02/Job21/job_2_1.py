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



class Book :

    def __init__(self,title,Author):
        self.title=title
        self.Author=Author

    def print(self):
        print("book title", self.title)

class Author(Person):
    def __init__(self, first_name, last_name):
        super().__init__(first_name,last_name)

        self.work = []

    def listerWork(self):
        if len(self.work) != 0 :
            print ("list of books by the author->" , self.first_name, " ", self.last_name)
            for book in self.work:
                print(book.title)

    def writeABook( self ,title):
        newbook= Book( title, self)
        self.work.append(newbook)
        return newbook
    
    