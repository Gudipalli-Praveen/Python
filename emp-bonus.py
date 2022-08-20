"""A company decided to give bonus to employee according to following criteria:
Time period of service           Bonus
More than 10 years                10%
>=6 and <=10                      8%
Less than 6 years                 5%
Ask user for their salary and year of service and print the net bonus amount"""

s = int(input("Enter a salary: "))
y = int(input("Enter a year: "))
if y > 10:
    bonus = 10/100*s
elif y >= 6 and y <= 10:
    bonus = 8/100*s
elif y < 6:
    bonus = 5/100*s
else:
    print("sorry")
print(bonus)