#########################################################
###################  TASK 2   ###########################
#########################################################

# Write and Append the data into file
import os

filename = 'output.txt'

user_int_input = int(input())

while user_int_input == 25:
    user_input = input("Type 'w/a/o/e' for write/append/output of file/exit from program respectively:\n").lower()


    def write():
        write_text = input("Enter text to write to the file: ")
        return write_text

    def append():
        append_text = input("Enter additional text to append: ")
        return append_text

    def final_content():
        print("Final content of output.txt:")
        file = open(filename, 'r')
        reading_file = file.readlines()
        print(reading_file)
        file.close()


    #Writing into file
    try:
        if user_input == 'w':
            try:
                file = open(filename,'w')
                writing_file = file.write(write())
                print('Data successfully written to output.txt.')
                file.close()
            except FileNotFoundError:
                print(f"Error: The file '{filename}' was not found.")

            #Appending into file
        elif user_input == 'a':
            try:
                file = open(filename,'a')
                appending_file = file.write(append())
                print("Data successfully appended.")
                file.close()
            except FileNotFoundError:
                print(f"Error: The file '{filename}' was not found.")

            #giving output of the file
        elif user_input == 'o':
            final_content()
            #print(content)
            os._exit(0)
        elif user_input == 'e':
            os._exit(0)
        else:
            print("Invalid input. Please type 'w' or 'a' or 'o' or 'e'")
            continue
    except IOError:
        print("Invalid input")
