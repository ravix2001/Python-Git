#walrus opetaror  :=

#happy = True
#print(happy)

#print(happy := True)        #use of walrus operator

#foods = list()
#while True:
#    food = input("What food do you like? : ")
#    if food == "quit":
#        break
#    foods.append(food)

foods = list()
while food := input("What food do you like? : ") != "quit":
    foods.append(food)