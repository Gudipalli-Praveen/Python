"""Creat a program that reads a duration from the user as a number of days,
hours, minutes, and seconds, Compute and display the total number of seconds
represented by this duration."""

#method:-1

"""a = int(input('Enter Number of Days: ')) * 3600 * 24
b = int(input('Enter Number of Hours: ')) * 3600
c = int(input('Enter Number of Minutes: ')) * 60
d = int(input('Enter Number of Seconds: '))

time =a + b + c + d
print(time)"""

#method:-2

days =int(input("Enter number of days: "))
hours =int(input("Enter number of hours: "))
min =int(input("Enter number of min: "))
sec =int(input("Enter number of sec: "))
d = days*24*60*60
h = hours*60*60
m = min*60
print("The total number of seconds ",d+h+m+sec)