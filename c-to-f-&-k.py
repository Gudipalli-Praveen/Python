"""Write a program that begins by reading a temperature from the user in degrees
celsius. Then program should display the equivalent temperatures in degrees
fahrenheit and degrees kelvin. The calculations needed to commen between defferent
units of temperature can be found on the internet """

c = int(input("Enter The Temperature in Celsius: "))
f = c*9/5 + 32
k = c + 273.15
print("in fahrenheit ", f )
print("in kelvin ", k)