def greet(fx):
    def mfx():
        print("Good Morning")
        fx()
        print("Thanks for visiting")
    return mfx

@greet
def hello():
    print("Hello!")

hello()

#greet(hello)()     #direct approach

#for arguments
def greet(fx):
    def mfx(*args, **kwargs):
        print("Good Morning")
        fx(*args, **kwargs)
        print("Thanks for visiting")
    return mfx

def add(a, b):
    print(a+b)

greet(add)(4,5)
