# for loop
n=int(input('Enter the number of terms: '))
a=0
b=1
for i in range(3,n+1):
    c=a+b
    print(c)
    a=b
    b=c


# while loop
n=int(input('Enter the number of terms: '))
a=0
b=1
while a<=n:
    c=a+b
    print(c)
    a=b
    b=c