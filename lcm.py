x=int(input('Enter X value: '))
y=int(input('Enter y value: '))
c=max(x,y)
while True:
    if c%x==0 and c%y==0:
        print('LCM ',c)
        break
    else:
        c=c+1