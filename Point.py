# This is a python code that define a class named Point

# p(x, y) -- a point

class Point:
    
    # The constructor
    def __init__(self, x, y):
        self.x = x
        self.y = y

    
    # 
    def dispPoint(self):
        print(f"({self.x}, {self.y})")


    # Overloading the + operator
    def __add__(self,other):
      return Point(self.x + other.x, self.y + other.y)


    # Overloading the - operator
    def __sub__(self, other):
        return Point(self.x - other.x, self.y - other.y)

     # Overloading the == operator
    def __eq__(self, other):
        if(self.x == other.x and self.y == other.y):
            return True
        else:
            return False




    # Destructor
    def __del__(self):
        class_name = self.__class__.__name__
        print (f"{class_name} destroyed")
          

# Instantiation of object
p1 = Point(2, 3)
p2 = Point(4, 8)
p1.dispPoint()
p2.dispPoint()

p3 = p1 + p2  # Using + operator overloading 
p3.dispPoint()

p4 = p1 - p2 # Using - operator overloading 
p4.dispPoint()

if(p1 == p2):
    print("They are equal")
else:
    print("They are not equal")


del p1
del p2
del p3