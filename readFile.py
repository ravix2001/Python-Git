#with open('file_name','r or w') as file:

try:
    with open('test.txt') as file:
        print(file.read())
except FileNotFoundError:
    print("File Not Found")