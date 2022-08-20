"""Position on a chess board are identified by a letter and a number. The letter identifies
the column, while the number identifies the row"""

n =int(input("Enter a number: "))
l =int(input("Enter a number: "))
if n%2==0 and l%2==0 or n%2!=0 and l%2!=0:
    print("Black")
else:
    print("White")