#import math
from math import pi
#from swampy.TurtleWorld import *

print("Hello Python 3!!",end="  ") # enters space after print
print("This is second line")

print("circumference of a circle is 2 * pi * r, so if r = 2, circumference : ", 2 * pi * 2)

# print new line 5 times
print("\n" * 5)
a = "last_name"

# substitute operator using {}.format 
print("first_name {}".format(a))

a = "left"
b = "right"

print(a,b, sep=' : ') 

year = 2020
event = 'Annual Funcion'
print(f'Let us celebrate {year} {event}')
