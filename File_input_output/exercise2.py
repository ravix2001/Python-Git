f = open("C:\\Users\\ravip_kww02zt\\Python-Git\\File_input_output\\practice.txt","r")
data = f.read()
print(data)
new_data = data.replace("Java","Python")
print(new_data)
f.close()

f = open("C:\\Users\\ravip_kww02zt\\Python-Git\\File_input_output\\practice.txt","w")
f.write(new_data)
f.close()

def searching():
    word = "learning"
    f = open("C:\\Users\\ravip_kww02zt\\Python-Git\\File_input_output\\practice.txt","r")
    search = f.read()
    if(search.find(word) != -1):
        print("Found")
    else:
        print("Not found")

searching()

def which_line():
    word = "programming"
    info = True
    line_no = 1
    f = open("C:\\Users\\ravip_kww02zt\\Python-Git\\File_input_output\\practice.txt","r")
    while info:
        info = f.readline()
        if(word in info):
            print(line_no)
            return
        line_no += 1
    print("-1")

which_line()