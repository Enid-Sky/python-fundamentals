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

