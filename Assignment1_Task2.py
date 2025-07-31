########################################################
##################  TASK 2 #############################
########################################################
#Taking First Name and Last Name from the user

first_name = input("Enter the first name: ").capitalize()
last_name = input("Enter the last name: ").capitalize()

#Performing concatination operations

def greetings(fname, lname):
  full_name = fname + " " + lname
  print(f"Hello, {full_name}! Welcome to the python programming.")

greetings(fname=first_name, lname=last_name)
