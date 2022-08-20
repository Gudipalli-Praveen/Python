"""Write a program to calculate the electricity bill (accept number of unit from user)
according to the following criteria
unit                  price
First 100 units        0
Next 100 units         RS 5 per unit
After 200 units        RS 10 per unit
(For example if input unit is 350 than total bill amount is Rs2000)"""

n = int(input("Enter number of units: "))
if n <= 100:
    bill = 0
elif n > 100 and n <= 200:
    bill= (n - 100)*5
else:
    bill = (n - 200)*10 + 500
print(bill)