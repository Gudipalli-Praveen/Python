"""Write a program that computes the body mass index (BMI) of an individual. your program should
begin by reading a height and weight from the user. Then it should use one of the following
two formulas to compute the BMI before displaying it. if you read the height in inches and
the weight in pounds then body mass index is computed using the following formula.

BMI = weight/(height*height)  * 703

if you read the height in meters and the weight in kilograms then body mass index is computed
using this slightly simply formula:

BMI = weight/height*height"""

weight = float(input("Enter your weight kg: "))
height = float(input("Enter your height m: "))
 
bmi = weight/height**2
print(bmi)