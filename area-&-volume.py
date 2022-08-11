"""Write a program that begins by reading a radius. r. from the user. The program will continue
by computing and displaying the area of a circle with radius r. and the volume of a sphere
with radius r. Use the pi constant in math module to your calculation"""

r = float(input("Enter radius value: "))
import math
ac = math.pi*r*r
vs = (4/3)*math.pi*(r**3)
print("The area of circle",ac)
print("The volume of sphere is",vs)