#File existence check by user(taking input as file path)
 
import os

path = input("Enter the path of file : ")
#path = "D:\\BrooCode.txt"

if os.path.exists(path):
    print("File exists")
    if os.path.isfile(path):
        print("It is a file.")
    elif os.path.isdir(path):
        print("It is a directory.")

else:
    print("File doesn't exist.")