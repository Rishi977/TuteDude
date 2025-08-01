#########################################################
###################  TASK 1   ###########################
#########################################################

#reading file with Handling exception
filename = 'sample.txt'
try:
    file = open(filename,'r')
    reading_file_line1 = file.readline()
    reading_file_line2 = file.readline()
    print("Reading file content:")
    print(reading_file_line1+""+reading_file_line2)
    file.close()
except FileNotFoundError:
    print(f"Error: The file '{filename}' was not found.")
