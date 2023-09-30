class Person:
    def __init__(self,name,firstname):
        self.__name=name
        self.__firstname= firstname
    @property
    def name(self):
      return self.__name
    @property
    def firstname(self):
      return self.__firstname


    def Sepresenter(self):
        print(self.firstname, self.name)    
person1 = Person("Jennifer","Lawrence")
person1.Sepresenter()        