"""In this exereise you will creat a program that reads a pressure from the user in kilopascals.
Once the pressure has been read your program should report the equivalent pressure in pounds
per square inch. millimeters of mercury and atmospheres. Use your research skills to 
determine the conversion factors between these units."""

kpa =float(input("Input pressure in kilopascals: "))
psi = kpa/6.89475729
mmhg = kpa * 760 / 101.325
atm = kpa / 101.325
print("The pressure in pounds per square inch: ",psi,"psi")
print("The pressure in millimeter of mercury: ",mmhg,"mmhg")
print("Atmosphere pressure:",atm,"atm")