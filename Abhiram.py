imple calculator
print("Simple calculator")
num1=float(input("enter the fisrt number:"))
num2=float(input("enter the secound number\:"))

print("1.Addition")
print("2.Subtraction")
print("3.Multiplication")
print("4.Division")
print("5,exit")

choose=int(input("enter the values form 1 to 5:"))

if choose==1:
  print("The addition of these two numbers are",num1+num2)
elif choose==2:
  print("The subtraction of these two numbers are",num1-num2)
elif choose==3:
  print("The multiplication of theese two numbers are",num1*num2)
elif choose==4:
  print("The division of these two numbers are",num1/num2)
elif choose==5:
  print("Thank you")
else:
  print("please choose a valid number")
