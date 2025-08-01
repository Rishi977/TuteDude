#################################################################
###################### TASK 2 ###################################
#################################################################

# Using Math module calculate some math operations

import math

number = int(input("Enter a number: "))

def square_root(num):
    if num < 1:
        return "Please enter the whole number greater than 0"
    else:
        sqr_root = math.sqrt(num)
        return sqr_root
    
def log_base_e(num):
    log_base = math.log(num)
    return log_base

def sin_radian(num):
    sin_of_number = math.sin(num)
    return sin_of_number

square_root_of_number = square_root(num=number)
log_base_e_of_number = log_base_e(num=number)
sin_radian_of_number = sin_radian(num=number)

print(f"Square root: {square_root_of_number}")
print(f"Logarithm: {log_base_e_of_number}")
print(f"Sine: {sin_radian_of_number}")
