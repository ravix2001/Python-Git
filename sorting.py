#sort() method   = used with lists
#sort() function = used with iterables

#students = ["Ram","Shyam","Hari","Krishna","Laxman"]        #lists

#students.sort()
#for i in students:
#    print(i)

#print("\n")

#students.sort(reverse=True)
#for j in students:
#    print(j)

#print("\n")

#students = ("Ram","Shyam","Hari","Krishna","Laxman")        #tuples        #iterables
#sorted_students = sorted(students)
#for i in sorted_students:
#    print(i)

#print("\n")

#sorted_students = sorted(students,reverse=True)
#for i in sorted_students:
#    print(i)

#print("\n")

students = [("Ram","F",60),
            ("Shyam","A",33),
            ("Hari","D",36),
            ("Krishna","B",20),
            ("Laxman","C",78)]
#grade = lambda grades:grades[0]
#grade = lambda grades:grades[1]
#grade = lambda grades:grades[2]

#students.sort(key=grade)
#students.sort(key=grade,reverse=True)

#for i in students:
#    print (i)

students = (("Ram","F",60),
            ("Shyam","A",33),
            ("Hari","D",36),
            ("Krishna","B",20),
            ("Laxman","C",78))
grade = lambda grades:grades[1]
sorted_students = sorted(students,key=grade)
for i in sorted_students:
    print(i)