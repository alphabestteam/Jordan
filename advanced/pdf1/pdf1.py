"""
1.Magic methods in Python are the special methods that start and end with the double underscores. 
 Magic methods are not meant to be invoked directly by you, but the invocation happens internally
from the class on a certain action.
__str__: To get called by built-int str() method to return a string representation of a type.
 __eq__:To get called on comparison using == operator.
__new__:	To get called in an object's instantiation.
__init__:	To get called by the __new__ method.

2. If we wont overwrite the __str__ function in the class, the object identification number.
3. If we do wont overwrite __eq__ function in a class, , two objects will be compared with their object's pointer rather than the object values.
4. The term "overloading operator" refers to the possibility for classes to implement special behavior for operators (such as +, -, *, / and so on). 
This is because operators for class objects can be used in a different way than we would for handling primitive types. For example, if we have a class that represents a rational number,
we can implement overloading operator for arithmetic operators such as +, -, *, / so that we can perform arithmetic operations on class objects the way we want.

the output at first didn't show me that the points are the same
"""



class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

point1 = Point(2, 3)
point2 = Point(2, 3)

if point1 == point2:
    print("points are the same")
else:
    print("points are different")

print(f"first point: ({point1.x}, {point1.y})")
print(f"second point: ({point2.x}, {point2.y})")

sum_point = Point(point1.x + point2.x, point1.y + point2.y)
print(f"point sum: ({sum_point.x}, {sum_point.y})")

