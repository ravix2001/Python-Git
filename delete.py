import os
path = "tobedeleted"
try:
    #os.remove(path)   //deletes a file
    os.rmdir(path)     #deletes an empty directory
    #shutil.rmtree(path) //deletes a directory containing files
except FileNotFoundError:
    print("File not found")
except OSError:
    print("Folder is not empty")
else:
    print(path+" deleted")