###################################################
################### TASK 2 ########################
###################################################

# Sum of integer from 1 to 50 using a loop

last_number = int(input("Enter the number till you want the sum: "))

def sum_of_integer(num):
    sum = 0
    for n in range(1, last_number+1):
        sum += n
    print(f"The sum of numbers from 1 to {last_number} is: {sum}")    

sum_of_integer(num=last_number)
