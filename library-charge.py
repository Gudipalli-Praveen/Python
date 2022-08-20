"""Accept the number of days from the user and calculate the charge for library according
to following:
Till five days:Rs 2/day.
six to ten days:Rs 3/day.
11 to 15 days:Rs 4/day.
after 15 days:Rs 5/day"""

n = int(input("Enter number of days: "))
if n<=5:
    a=n*2
    print(a)
elif n<=10:
    b=n*3
    print(b)
elif n<=15:
    c=n*4
    print(c)
else:
    d=n*5
    print(d)