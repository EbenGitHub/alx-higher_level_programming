#!/usr/bin/python3

class User:
     def __init__(self, name="", sex='', age=""):
             self.name = name
             self.age = age
             self.sex = sex

     @property
     def age(self):
             print("Decrypting Age")
             return self.__age
     @age.setter
     def age(self, value):
             if (value <= 50 and value >= 21):
                 self.__age = value
             else:
                 print("Not allowed here")

     @property
     def sex(self):
             print("Decrypting sex")
             return self.__age
     @sex.setter
     def sex(self, value):
             if (value == 'M' or value == 'm' or value == 'F' or value == 'f'):
                 self.__sex = value
             else:
                 print("Not the correct sex")

def main():
     aUser = User("He", 'M', 32)
     bUser = User("she", 's', 32)

     print("{} {} {}".format(aUser.name, aUser.age, aUser.sex))

main()
