# Python Inheritance

# Parent Class

class Person:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname
        
    def	printname(self):
        print(self.firstname, self.lastname)
        
x = Person("Panupong", "Mikada")
x.printname()
print("--------------------")

# Create a Child Class

class Mychild(Person):
    pass

x = Mychild("Mi", "kada")
x.printname()
print("--------------------")

# Add the __init__() Function

class Student(Person):
    def __init__(self, fname, lname):
        Person.__init__(self, fname, lname)
        
x = Mychild("Mi", "Mikada")
x.printname()
print("--------------------")

# Use the super() Function

class Student(Person):
    def __init__(self, fname, lname):
        super().__init__(fname, lname)
        
x = Mychild("Mikada", "Panupong")
x.printname()
print("--------------------")

# Add Properties, Add Methods

class Student(Person):
    def __init__(self, fname, lname, year):
        super().__init__(fname, lname)
        self.year = year
    
    def welcome(self):
        print("Welcome", self.firstname, self.lastname, "to the class of", self.year)
        
x = Student("Mike", "Olse", 2019)
x.welcome()
print("--------------------")