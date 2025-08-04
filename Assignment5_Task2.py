###############################################
#################  TASK - 2 ###################
###############################################

#Creating a list from 1 to 10
numbers = [1,2,3,4,5,6,7,8,9,10]

#printing original list
print(f"Original list: {numbers}")

print(f"Extracted first five elements: {numbers[0:5]}")

my_list = []
for n in range(1,6):
    my_list.append(n)
reversed_list = list(reversed(my_list))

print(f"Reversed extracted elements: {reversed_list}")
