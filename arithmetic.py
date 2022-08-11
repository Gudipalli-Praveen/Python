"""Create a program that reads two integers, a and b. from the user. Your program should 
compute and display

The sum of a and b
The difference when b is subtracted from a
The product of a and b
The quotient when a is divided by b
The reminder when a is divided by b
The result of log(10)a
The result of a**b"""

a = int(input("Enter 1st number: "))
b = int(input("Enter 2nd number: "))
c = a + b
d = a - b
e = a * b 
f = a / b
g = a % b
h = a ** b
import math
i = math.log(a)
print(c,d,e,f,g,h,i,sep="\n")