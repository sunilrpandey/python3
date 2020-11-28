import sys
import os

class Animal:
    __name = ""
    __sound = ""
    __height = 0

    def __init__(self, name, sound, height) :
        self.__name = name
        self.__sound = sound
        self.__height = height

    def set_name(self, value) :
        self.__name = value

    def set_height(self, value) :
        self.__height = value

    def set_sound(self, value) :
        self.__sound = value

    def get_name(self) :
        return self.__name

    def get_height(self) :
        return self.__height

    def get_sound(self) :
        return self.__sound

    def get_type(self):
        print("Animal")
    
    def to_string(self) :
        return "This is {}, of hight - {} and I say - {}".format(self.__name, self.__height, self.__sound)


class Dog(Animal):
    __owner = ""

    def __init__(self, name, sound, height,owner):
        self.__owner = owner
        super(Dog, self).__init__(name,sound,height)

    def set_owner(self, owner) :
        self.__owner = owner

    def get_owner(self):
        return self.__owner

    def get_type(self):
        print("Dog")

    def to_string(self):
        return "{} is of height - {} and says - {} and owner is - {}"\
                    .format(self.get_name(), self.get_height(),self.get_sound(),self.get_owner())


class AnimalTesting:
    def get_type(self, animal):
        animal.get_type()

def demo_class():
    cat = Animal("Pooshy","Meow",20)
    print(cat.to_string())

    dog = Dog("Tommy","Bark",30, "Master")
    print(dog.to_string())

    test_animals = AnimalTesting()
    test_animals.get_type(cat)
    test_animals.get_type(dog)

if __name__ == "__main__":
    demo_class()
    #demo_reusability()
