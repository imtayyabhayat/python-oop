from app.services.books import Books

book = Books("J.K.Rowling", "Harry Potter", "1997", "123456789")

print(book.display())

"""
this code is the basic example of polymorphism.
keep it safe
"""
# class Animal:
#     def sound(self):
#         pass

# class Dog(Animal):
#     def sound(self):
#         return "Woof!"

# class Cat(Animal):
#     def sound(self):
#         return "Meow!"

# class Cow(Animal):
#     def sound(self):
#         return "Moo!"

# # Polymorphic function
# def make_sound(animal):
#     print(animal.sound())

# # Creating instances of different classes
# dog = Dog()
# cat = Cat()
# cow = Cow()

# # Calling the polymorphic function with different objects
# make_sound(dog)  # Output: Woof!
# make_sound(cat)  # Output: Meow!
# make_sound(cow)  # Output: Moo!
