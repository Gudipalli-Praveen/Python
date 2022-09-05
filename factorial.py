# For Loop

from re import I


n=int(input("Enter any number: "))
j=1
for i in range(1,n+1):
    j=j*i
print(j)


# While Loop

n=int(input("Enter any number: "))
i=1
j=1
while i<=n:
    j=j*i
    i=i+1
print(j)