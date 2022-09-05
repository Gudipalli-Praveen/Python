"""A particular cell phone plan includes 50 minutes if air time and 50 text messages for $15.00
a month. Each additional minute of air time costs $0.25. while additional text messages cost
$0.15 each. All cell phone bills include an additional charge of $0.44 to support 911 call center,
and the entire bill (including the 911 chaege) is subject to 5 percent sales tax.

   Write a program that reads the number of minutes and text messages used in a month from the
user. Display the base charge, additional minutes charge(if any),additional text message charge
(if any), the 911 fee, tax and total bill amount. Only display the additional minute and text
message charges if the user incurred costs in these categories."""

a = int(input("Enter a additional minutes: "))
b = int(input("Enter a additional text messages: "))

if a>50 and b>50:
   min=((a-50)*0.25)+((b-50)*0.15)
   print("$",min)
else:
   print("Free")