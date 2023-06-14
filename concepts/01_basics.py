# import math
from math import pi

# from swampy.TurtleWorld import *

def override_endOfLine():
    print("Hello Python 3!!, new line after print is overriden by ___", end="___")  # enters space after print
    print("Should have been on new line but will be after new end character")
    print("this line will come after new line if default'end' is not overridden in above print statement")

def override_separator():
    # override separator using sep = 
    print("override separator")
    a = "left"
    b = "right"
    print(a, b, sep=" : ")

def create_string_using_format():
    print("substitute variables using {}.format")
    a = "last_name"
    print("first_name {}".format(a))
    
    print("use \"f\" instead of format, {} and variables :")
    year = 2020
    event = "Annual Funcion"
    print(f"Let us celebrate {year} {event}")

    
def print_demo():
    override_endOfLine()
    override_separator()
    create_string_using_format()
    
    print("print new line 5 times","\n" * 5)
    return ;
    

if __name__ == "__main__":
    print("Demo will show some print options such as \nseparatator \nendline char \nplaceholder{}")
    print_demo()
    x = 12
    print(f"x is {x}")

else:
    print("File is being imported.")
