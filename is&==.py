a = 4
b = "4"
c = 4
d = [1,2,3]
e = [1,2,3]

print(a is b)       #exact location of object in memory
print(a == b)       #value

print(a is c)       #exact location of object in memory
print(a == c)       #value

print("Checking list")
print(d is e)
print(d == e)