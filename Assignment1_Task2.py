########################################################
##################  TASK 2 #############################
########################################################
#Taking First Name and Last Name from the user

first_name = input("Enter the first name: ").captalize()
last_name = input("Enter the last name: ").captalize()

#Performing concatination operations

def greetings(fname, lname):
  full_name = fname + " " + lname
  print("Hello, {full_name}! Welcome to the python programming.")

greetings(fname=first_name, lname=last_name)
