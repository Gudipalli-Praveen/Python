"""Creat a program that reads three integers from the user and displays them in sorted
order (from smallest to largest).Use the min and max functions to find the smallest
and largest values. The middle value can be found by computing the sum of all three
values. and then subtracting the minimum value and the maximum value."""

n1 = int(input('Enter 1st Number: '))
n2 = int(input('Enter 2nd Number: '))
n3 = int(input('Enter 3rd number: '))

a1 =min(n1,n2,n3)
a3 =max(n1,n2,n3)
a2 =(n1+n2+n3)-a1-a3

print(a1,a2,a3,sep="\n")