# For loop

n = int(input("Enter the n value: "))
s = 0
for i in range(1,n+1):
   a = int(input("Enter next number: "))
   s = s + a
avg = s/n
print(avg)


# While loop

n = int(input("Enter the n value: "))
total_numbers = n
sum = 0
while n > 0:
    a = int(input("Enter a value: "))
    sum = sum + a
    n -= 1
avg = sum / total_numbers
print(avg)