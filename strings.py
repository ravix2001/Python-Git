name="Ravi"
surname="Pandit"

string='''He said,"He is an Engineer"
          and his brother is a Doctor.''' 

print("Hello,", name , surname)

print('He said,"He is an Engineer"')

print(string)

print(name[0])
print(name[1])
print(name[2])
print(name[3])
#print(name[4])
#print(name[5])

print("Let's use for loop")
for character in name:
    print(character)
print("\n")
for character in string:
    print(character)

#slicing() or indexing[]  print(string[start:stop:step])