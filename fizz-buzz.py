'''Write a program to print the numbers in following formet
1) If the number is divisible by 3 it has to print 'FIZZ'
2) If the number is divisible by 5 it has to print 'BUZZ'
3) If the number is divisible by 3 and 5 it has to print 'FIZZ BUZZ'
4) other wise print the number.
Consider the numbers from 1 to 100.'''

# for loop

for i in range(1,201):
    if i%3==0 and i%5==0:
        print('FIZZ BUZZ')
    elif i%3==0:
        print('FIZZ')
    elif i%5==0:
        print('BUZZ')
    else:
        print(i)

# while loop

n=0
while n<201:
    n+=1
    if n%3==0 and n%5==0:
        print('FIZZ BUZZ')
    elif n%3==0:
        print('Fizz')
    elif n%5==0:
        print('BUZZ')
    else:
        print(n)