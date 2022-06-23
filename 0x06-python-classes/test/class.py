#!/usr/bin/python3

class Dog:

    def __init__(self, name="", height=0, weight=0):
        self.name = name
        self.height = height
        self.weight = weight

    def run(self):
        print("{} runs".format(self.name))

    def eat(self):
        print("{} eats".format(self.name))

    def bark(self):
        print("{} barks".format(self.name))

def main():
    spot = Dog("Spot", 45, 23)
    spot.run()
    spot.eat()
    spot.bark()

    bowser = Dog("Bowsei", 23, 32)
    bowser.bark()
    bowser.eat()
    bowser.run()

main()
