"""Develop a program that begins by reading a number of seconds from the user. Then your
program should display the equivalent amount of time in the form D:HH:MM:SS. where D.
HH.MM.and SS represent days,hours,minutes and seconds respectively.The hours
minutes and seconds should all be formatted so that they occupy exactly tho digits.
Use your research skills determine what additional character need to be included in
the format specifier so that leading zeros are used instead of leading spaces when a
number is formatted to a particular width."""

#method:-1

"""num = int(input("Enter Seconds: "))
hour = num//3600
hour1 = num%3600
min = hour1//60
sec = hour1%60
print("Hours: ",hour,"min",min,"sec",sec)"""

#method:-2

s = int(input("Enter number of seconds: "))
d = s// (24*60*60)
s = s% (24*60*60)
h = s// (60*60)
s = s% (60*60)
m = s// (60)
s = s%(60)
s = s
print(d,h,m,s,sep=":")