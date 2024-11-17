class Person:
    name = "anonymous"

    #def changeName(self, name):
        #self.name = name it was printing the name anyonomus instead of ayesha
       # Person.name = name
     #  self.__class__.name = "ayesha"

    @classmethod
    def changeName(cls, name):
        cls.name = name

p1 = Person()
p1.changeName("ayesha")
print(p1.name)
print(Person.name)