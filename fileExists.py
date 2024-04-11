#Check whether the file exists or not

import os

path = "D:\\BroCode.txt"
#path = "D:\\BrooCode.txt"

if os.path.exists(path):
    print("File exists")
    if os.path.isfile(path):
        print("It is a file.")
    elif os.path.isdir(path):
        print("It is a directory.")

else:
    print("File doesn't exist.")