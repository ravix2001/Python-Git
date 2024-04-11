text = "\nHello Bro \nWelcome to Python Programming....."
#with open('test.txt','w') as file:
#    file.write(text)

# w mode erases previous data so append mode is better to use if we want to add something in previous file as

with open('test.txt','a') as file:
    file.write(text)