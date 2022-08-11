"""Many people think about their height in feet and inches,even in some countries that primarily
use the metric system Write a program that reads a number of feet from the user, followed 
by a number of inches. Once these values are read. Your program should compute and display
the equivalent number of centimeters."""

f = float(input("Enter number of feet: "))
i = float(input("Enter number of inches: "))

a = f * 12 * 2.54
b = i * 2.54

print(a+b)