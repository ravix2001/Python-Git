#indexing
name ="Bro Code"
name1 = name[0]
print (name1)
name2 = name[0:3]
print (name2)
name3 = name[0:8:2]
print (name3)
print("\n")
first_name = name[0:3]
print(first_name)
last_name = name[4:8]
print(last_name)
reversed_name = name[::-1]
print(reversed_name)

#slicing
website1 = "https://google.com"
website2 = "https://facebook.com"
#slice = slice(8,14)
#slice = slice(8,14,1)
slice = slice(8,-4)
print(website1[slice])
print(website2[slice])
