########################################################
##################  TASK 1 #############################
########################################################
#Taking numbers from the user

number1 = int(input("Enter the first number: "))
number2 = int(input("Enter the second number: "))

#Performing arthmetic operations

#ADDITION
def addition(num1, num2):
  sum = num1 + num2
  print(f"The sum of {num1} and {num2} is: {sum}")

#SUBTRACTION
def subtraction(num1, num2):
  sub = num1 - num2
  print(f"The subtraction of {num1} and {num2} is: {sub}")

#DIVIDISON
def divide(num1, num2):
  div = num1 / num2
  print(f"The division of {num1} and {num2} is: {div}")

def multiplication(num1, num2):
  mul = num1 * num2
  print(f"The sum of {num1} and {num2} is: {mul}")

addition(num1=number1, num2=number2)
subtraction(num1=number1, num2=number2)
divide(num1=number1, num2=number2)
multiplication(num1=number1, num2=number2)
