"""Develop a program that reads a four-digit integer from the user and displays the sum
of its digits. For example.if the user enters 3141 then your program should display
3+1+4+1=9"""
a = int(input("Enter any four digits of Number: "))
f = a//1000
f1 = a%1000
s = f1//100
s1 = f1%100
t = s1//10
t1 = s1%10
print(f , s , t , t1)
