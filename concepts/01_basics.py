# import math
from math import pi

# from swampy.TurtleWorld import *


def print_demo():
    print("Hello Python 3!!, new line after print is overriden by ___", end="___")  # enters space after print
    print("Should have been on new line but will be after new end character")

    print("this line will come after new line if default'end' is not overridden in above print statement")

    # print new line 5 times
    print("print new line 5 times")
    print("\n" * 5)
    
    # override separator using sep = 
    print("override separator")
    a = "left"
    b = "right"
    print(a, b, sep=" : ")

    # substitute variables using {}.format
    print("substitute variables using {}.format")
    
    a = "last_name"
    print("first_name {}".format(a))

    
    print("use f instead of format, {} and variables")
    year = 2020
    event = "Annual Funcion"
    print(f"Let us celebrate {year} {event}")


if __name__ == "__main__":
    print("Demo will show some print options such as \nseparatator \nendline char \nplaceholder{}")
    print_demo()
else:
    print("File is being imported.")
