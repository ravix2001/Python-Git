import random

x = random.randint(1,6)
y = random.random()

print("\n",x)
#print(y)

myList = ['Rock','Paper','Scissor']
z = random.choice(myList)
#print(z)

cards = ['A',2,3,4,5,6,7,8,9,10,'J','Q','K']
random.shuffle(cards)

#print(cards)