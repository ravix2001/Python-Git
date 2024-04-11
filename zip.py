#zip(*iterables) = aggregate elements from two or more iterables (list, tuples, sets, etc.)
#                    creates a zip object with paired elements stored in tuples for each element

usernames = ["Ram", "Shyam", "Hari"]
passwords = ("p@ssword", "@bc123", "@dmin")

users = zip(usernames, passwords)
print(type(users))
for i in users:
    print(i)