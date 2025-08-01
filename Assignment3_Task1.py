#################################################################
###################### TASK 1 ###################################
#################################################################

# Calculate Factorial using a function

number = int(input("Enter a number: "))

def factorial(num):
    if num < 2:
        return 1
    else:
        fact = num * (factorial(num-1))
        return fact
    
num_fact = factorial(num=number)
print(f"Factorial of {number} is: {num_fact}")
