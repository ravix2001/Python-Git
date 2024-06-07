class person:
    name = input("Enter the name : ")
    occupation = input("Enter the occupation : ")
    networth = input("Enter the networth : ")
    def info(self):             #default constructor
        print(f"{self.name} is a/an {self.occupation}.")


a = person()

print(a.name)
print(a.occupation)
print(a.networth)
a.info()

b = person()

b.name = "harry"
b.occupation = "doctor"
b.networth = "5000"

print(b.name)
print(b.occupation)
print(b.networth)
b.info()

