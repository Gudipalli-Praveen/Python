"""The following table contains earthquake magnitude range on the Richter scale and their
descriptors:

        Magnitude                              Descriptor
    Less than 2.0                               Micro
    2.0 to less than 3.0                        Very Minor
    3.0 to less than 4.0                        Minor
    4.0 to less than 5.0                        Light
    5.0 to less than 6.0                        Moderate
    6.0 to less than 7.0                        Strong
    7.0 to less than 8.0                        Major
    8.0 to less than 10.0                       Great
    10.0 or more                                Meteorie
    
    Write a program that reads a magnitude from the user and displays the appropriate descriptor
as part of a meaningful message. For example, if the user enters 5.5 than your program should
indicate that a magnitude 5.5 earthquake is considered to be a moderate earthquake."""

r = float(input("Enter a range: "))
if r<2.0:
    print("Micro")
elif r>2.0 and r<3.0:
    print("Very Minor")
elif r>3.0 and r<4.0:
    print("Minor")
elif r>4.0 and r<5.0:
    print("Light")
elif r>5.0 and r<6.0:
    print("Moderate")
elif r>6.0 and r<7.0:
    print("Strong")
elif r>7.0 and r<8.0:
    print("Major")
elif r>8.0 and r<10.0:
    print("Great")
else:
    print("Meteorie")