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
    
    

class Customer(Person):
    def __init__(self, first_name, last_name):
        super().__init__(first_name, last_name)
        self.book_collection = []

    def inventory (self):
            print(self.book_collection)

class Library:

    def __init__(self, name):
        self.name = name
        self.catalog=[]
        self.quantity=0

    def buyBook (self,author, title, quantity ):

        for books in author.work: 
            if books.title == title:

                newbooks= [Book(title, Author), quantity]
                self.catalog.append(newbooks)

    def inventory (self):
        for b in self.catalog:
            print("the inventory of the librairy :", "(", b[0].title,", quantité :", b[1] , ")")

    def rent(self, client, title):
        for b in self.catalog:
            if b[0].title == title and b[1]>0 :
                client.book_collection.append(b[0].title)
                b[1]-= 1
    def renderbooks(self,client):
        for b in client.book_collection:
            i=0
            for b2 in self.catalog:
                i+=1
                if b2[0].title== b:
                    client.book_collection.remove(b)
                    b2[1]+= 1