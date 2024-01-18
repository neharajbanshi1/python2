class Robot:
    new_var ="this is token"
    
robot = Robot()
print (robot.new_var)

#constructor
class Fruits:
    def __init__(self,name:str,price:int):
        self.name=name
        self.price=price
    def __str__(self) -> str:
        return f"this fruit is {self.name} and price is {self.price}"
    def getFruitValues(self):
        return f"this is fruit value"
fruit = Fruits("mango",200)
fruit1= Fruits("Orange", 600)
print(fruit)
print(fruit1)

#INHERITANCE

class Music:
    def playMusic(self):
        return "Music has been started"
class Guitar(Music):
    def guitarMusic(self):
        return "tuntuntuntun"
    
guitar = Guitar()
print(guitar.guitarMusic())
print(guitar.playMusic())

#staticmethod

class StaticExample():
    @staticmethod
    def guitarMusic():
        return "tuntuntuntun"
print(StaticExample.guitarMusic())