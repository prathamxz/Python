class person:
    name="pratham"
    occupation = "Student"
    networth = 10
    def info(self):
        print(f"{self.name} is a {self.occupation}")
a = person()
b = person()

a.name = "Shubham"
# print(a.name)
a.occupation = "ca"
# print(a.occupation)
a.info()

b.name = "Nitin"
b.occupation="accountant"


a.info()
b.info()









# Python Class and Objects

# A class is a blueprint or a template for creating objects, providing initial values for state (member variables or attributes), and implementations of behavior (member functions or methods). The user-defined objects are created using the class keyword.Creating a Class:
# Let us now create a class using the class keyword.
# class Details:
# name = "Rohan"
# age = 20
# Creating an Object:
# Object is the instance of the class used to access the properties of the class Now lets create an object of the class.



# self parameter
# The self parameter is agreference to the current instance of the class, and is used to access variables that belongs to the class.
# It must be provided as the extra parameter inside the method definition.
# Example:
# class Details:
# name =
# "Rohan"
# age = 20
# def desc(self):
# print( "My name is", self.name,
# "and I'm", self.age,
# "years old.")
# obj1 = Details()
# obj1. desc()