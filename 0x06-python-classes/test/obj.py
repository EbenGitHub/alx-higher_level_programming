#!/usr/bin/python3

class Robot:
    population = 0

    def __init__(self, name):
        self.name = name
        print("Initializing {}".format(self.name))
        Robot.population += 1

    def die(self):
        print("{} is being destroyed".format(self.name))
        Robot.population -= 1

        if Robot.population == 0:
            print("{} was the last one.".format(self.name))
        else:
            print("There are still {:d} robots working.".format(Robot.population))

    def say_hi(self):
        print("Greeting, name he {}.".format(self.name))
    @classmethod
    def how_many(cls):
        print("We have {:d} robots.".format(cls.population))

rob1 = Robot("r1")
rob1.say_hi()
Robot.how_many()

rob2 = Robot("r2")
rob2.say_hi()
Robot.how_many()

rob3 = Robot("r3")
rob3.say_hi()
Robot.how_many()

print("\nRobots can do some work here.\n")
print("Robots have finished their work. so destryoy them.")
rob1.die()
rob2.die()
rob3.die()
Robot.how_many()
