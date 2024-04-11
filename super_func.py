#super() = function used to give acess to the methods of a  parent class
#            Returns a temporary object of a parent class when used

class rectangle:                            #parent class
    def __init__(self,length,width):        #constructor
        self.length = length
        self.width = width

class square(rectangle):                    #child class
    def __init__(self,length,width):
        super().__init__(length,width)
    def area(self):
        return self.length*self.width
    
class cube(rectangle):                      #child class
    def __init__(self, length, width,height):
        super().__init__(length, width)
        self.height = height
    def volume(self):
        return self.length*self.width*self.height

obj1 = square(3,3)
obj2 = cube(3,3,3)

print(obj1.area())
print(obj2.volume())
