# Method Overriding: Customizing Inherited Behavior
# Method overriding is how polymorphism is achieved in inheritance. When a child class defines a method with the same name as a method in its parent class, the child's version overrides the parent's version for objects of the child class. This allows specialized behavior in subclasses. The parent class's method is still available (using super()), but when you call the method on a child class object, the child's version is executed.

# Operator Overloading: Making Operators Work with Your Objects
# Python lets you define how standard operators (like +, -, ==) behave when used with objects of your own classes. This is done using special methods called "magic methods" (or "dunder methods" because they have double underscores before and after the name).

class Point:
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def sum(self, p):
        return Point((self.x + p.x) , (self.y + p.y))
    
    def print_point(self):
        print (f"x is {self.x} and y is {self.y}" )
    
    def __add__ (self, p):
        return Point((self.x + p.x) , (self.y + p.y))

p1 = Point(5,3)
p2 = Point(2,9)

# p = p1.sum(p2)# Return a new point which is sum of p1 and p2 
p = p1 + p2
p.print_point()