a =int(input("Enter x**2 coefficent: "))
b =int(input("Enter x coefficent: "))
c =int(input("Enter constant: "))

delta =((b**2)-(4*a*c))**0.5
if delta >= 0:
    root1 =(-b+delta)/2*a
    root2 =(-b-delta)/2*a
    print("The root of given equation are",root1,root2,sep=",")
else:
    print("The root are complex")