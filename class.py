#coding=utf-8
import sys
reload(sys)
sys.setdefaultencoding('utf8')

# #p141
# class Dog():
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def sit(self):
#         print (self.name.title() + " is now sitting.")

#     def roll_over(self):
#         print (self.name.title() + " rolled over!")

# my_dog = Dog('Willie','6')
# Dog.sit(my_dog)
# Dog.roll_over(my_dog)
# print ("my dog is " + my_dog.age + " years old.")
# my_dog.sit()
# my_dog.roll_over()

#9-1/9-2
# class Restaurant():
#     def __init__(self, restaurant_name, cuisine_type):
#         self.name = restaurant_name
#         self.cuisine = cuisine_type

#     def describe_restaurant(self):
#         print (self.name + " & " + self.cuisine + ".")

#     def open_restaurant(self):
#         print ("The" + self.name + "is openning.")

# restaurant_A = Restaurant('GoodTaste', 'Chinese')
# restaurant_B = Restaurant('Sushi', 'Japanese')
# restaurant_C = Restaurant('Pizza', 'Italian')

# restaurant_A.describe_restaurant()
# restaurant_A.open_restaurant()
# restaurant_B.describe_restaurant()
# restaurant_B.open_restaurant()
# restaurant_C.describe_restaurant()
# restaurant_C.open_restaurant()

#9-3
# class User():
#     def __init__(self, f_name, l_name):
#         self.first_name = f_name
#         self.last_name = l_name

#     def describe_user(self):
#         print ("This is " + self.first_name + " " + self.last_name + ".")

#     def greet_user(self):
#         print ("Hello, " + self.first_name + " " + self.last_name + ".")

# Ken = User('Ken', 'Vincent')

# Ken.describe_user()
# Ken.greet_user()