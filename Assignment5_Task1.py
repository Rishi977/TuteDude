###############################################
#################  TASK - 1 ###################
###############################################

#Creating student dictonary
student = {'Rishikesh':'98','Vishal':'95','Prince':'99','Tanmay':'97'}

student_name = input("Enter the student's name: ").capitalize()

if student_name in student:
    print(f"{student_name}'s marks: {student[student_name]}")
else:
    print("Student not found.")
