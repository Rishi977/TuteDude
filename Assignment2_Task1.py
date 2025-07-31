###################################################
################### TASK 1 ########################
###################################################

#Checking whether the input number is even or odd.

num = int(input("Enter a number: \n"))

def check_even_odd(number):
    if number % 2 == 0:
        print(f"{number} is an even number.")
    else:
        print(f"{number} is an odd number.")

check_even_odd(number=num)
