import os

source = "move.txt"
destination = "D:\\move.txt"

try:
    if os.path.exists(destination):
        print("File already exists")
    else:
        os.replace(source,destination)
        print(source+" moved")
    
except FileNotFoundError:
    print(source+" not found")