# Define a class

class Musician:
    pass


# Instantiate a class


drummer = Musician()



# Create class variables of title and instruments

class Musician:
    title = "Rockstar"
    instruments = True
        
drummer = Musician()
print(drummer.title)
print(drummer.instruments)


# Create a method describing NY housewives

class Housewife:
    
    house = "Home in the Hamptons"
    money = "Self Made"
    famous = "Being on TV"
    tired_of_hearing = "The word Jovani"
    
    def known_for(self):
        print(f"She is known for having a {self.house}, and claiming she is a {self.money} millionarie.")
        
luanne = Housewife()
luanne.known_for()    

# Create a method with arguements: create a program that calculates the area of a circle. Create a Circle class with class varible of pi. Set pi to 3.14

class Circle:
    pi = 3.14

    def area(self, radius):
        return self.pi * radius **2

circle = Circle()

pizza_area = circle.area(12/2)
teaching_table_area = circle.area(36/2)
round_room_area = circle.area(11460/2)
print(pizza_area, teaching_table_area, round_room_area)

# Create a store class and add two instance variables

class Store:
      pass

alternative_rocks = Store()
isabelles_ices = Store()

alternative_rocks.store_name = "Alternative Rocks"
isabelles_ices.store_name = "Isabelle's Ices"


# Check to see if the elem in the list have a count attribute

can_we_count_it = [{'s': False}, "sassafrass", 18, ["a", "c", "s", "d", "s"]]

for elem in can_we_count_it:
  if hasattr(elem, "count"):
    print(f"{type(elem)} has the count attribute!")
  else:
    print(f"{type(elem)} does not have the count attribute :(")


# Define a secure method on SearchEngineEntry class that returns the secure link to an entry

class SearchEngineEntry:
    secure_prefix = "https://"
    def __init__(self, url):
        self.url = url
 
    def secure(self):
        return "{prefix}{site}".format(prefix=self.secure_prefix, site=self.url)
 
codecademy = SearchEngineEntry("www.codecademy.com")
wikipedia = SearchEngineEntry("www.wikipedia.org")
 
print(codecademy.secure())
# prints "https://www.codecademy.com"
 
print(wikipedia.secure())
# prints "https://www.wikipedia.org"



# Define a class student, add a constructor that takes in two parameters of name and year. Create three instances of the class student(student names). Create a class with Grade and add a constructor which takes in a score. Go to Student class and declare a self.grades attribute as an empty list. Ass a method to add grades to Student that takes a parameter grade. It should verify if the type Grade is the same and if so add the grade. Create a new Grade with a score of 100 and add it to pieter's grade attribute using add_grade. 


class Student:
    def __init__(self, name, year):
        self.name = name
        self.year = year
        self.grades = []
  
    def add_grade(self, grade):
        if type(grade) is Grade:
            self.grades.append(grade)      

class Grade:
    minimum_passing = 65
  
    def __init__(self, score):
        self.score = score
    
roger = Student("Roger van der Weyden", 10)
sandro = Student("Sandro Botticelli", 12)
pieter = Student("Pieter Bruegel the Elder", 8)
pieter.add_grade(Grade(100))