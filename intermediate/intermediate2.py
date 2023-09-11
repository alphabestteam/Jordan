"""
imports:
import is a Python concept used to import modules or parts of other modules into the current code file. It is useful when you want to use functions,
variables or classes that are in modules that are not part of the current module you are working with.

When you import from another file in Python, you must provide the exact path to the file you are trying to import.
The path may be relative to the current location of the code file you are working on.
If the module file you are trying to import is in the same location as your code file, you can write: import mymodule
If the module file is in a subfolder that is more correct than your code file, use a relative path, for example: import mymodule.submodule
If the module file is outside the folder where your code file is, you'll need to use an absolute path like this: import some_module.submodule

The condition `if __name__ == "__main__":` is a condition used in Python to check if the current file is 
run directly as a main program or if it is imported as a module into another file.
The condition `if __name__ == "__main__":` allows you to execute code only when the file is run directly as a main program and not when it is imported as a module into another file.
This prevents code from being executed every time it is imported and allows you to run it independently or combine it inside another file as a module.

 
classes:
Classes are a structure in which objects can be defined. A class defines the attributes (variables) and actions (functions) of the objects that have the same type 
and originate in the defined class. Each object holds its own individual variables in its state, but it inherits the actions of the class.

Classes help organize the code into separate units. which improves code readability.
Departments allow different teams to develop separate parts of the code relatively independently, without knowing the internal details of each part.
In addition, classes can produce renewed classes from existing classes, where the new class inherits the features and actions of the existing class.

An attribute of a class is a variable that is inside the class and is used to describe attributes or characteristics that are attributed to objects created from the class.
These attributes contain information or data related to objects created from the class, and they can be numbers, strings, or other objects, depending on the need.

An object of a class represents a specific entity with properties and attributes defined in the class.
Such an object contains the specific information for that entity or object, and is able to perform actions that are allowed to it according to the definition in the class.

Constructor: A constructor is a method within a class in object-oriented programming used to create an instance of that class.
It is called when a new object is created and initializes the required variables of the class. In Python, the constructor is the __init__() method.

Destructor: A destructor is a method used in object-oriented programming to handle the cleanup or finalization of an object's resources when its lifetime ends. 

The term "self" is used in the context of classes and refers to the object itself created from a class. In practice,
"self" is a state manager variable that adds privacy to variables and functions within the class. When an object is created from a class, 
"self" is the object itself, and it allows you to use its attributes and functions within the class.

Inheritance is a principle in object programming that allows you to create a new class by using the attributes and actions found in an existing class. 
The successor class lists the features and actions of the "parent" class and can add or change them as needed.

Polymorphism is a principle in object programming that allows objects belonging to different classes to respond differently to the
same operation or query. Polymorphism provides great flexibility in the design and use of code,
allowing to write general code that can operate on a wide variety of objects and behave according to the specific object type.

A static attribute and a static function are attributes in classes different from normal (non-static) attributes, and they are used to access data or functions 
that are at the level of the entire class and not in objects from it.

The main differences between a static attribute/function and a regular attribute/function are:
Access: Static attributes and static functions are accessible from the class level itself and not from particular objects. This means that you can access them even without creating an object from the class.
Usage: Static attributes and static functions sound to be a good alternative to regular functions or regular attributes when you want to store information 
that is shared by the entire class and does not depend on certain objects.
It can be used for example to provide general information for a class or to perform actions for a class that do not depend on the status of certain objects.
static attribute: static_var = 0 
static function:
@staticmethod
    def static_method():
        print("hello")
"""
import random
class Person:
    def __init__(self, name, id_number, age):
        self.name = name
        self.id_number = id_number
        self.age = age

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def get_id_number(self):
        return self.id_number

    def set_id_number(self, id_number):
        self.id_number = id_number

    def get_age(self):
        return self.age

    def set_age(self, age):
        self.age = age

    def print_info(self):
        print(f"Name: {self.name}")
        print(f"ID: {self.id_number}")
        print(f"Age: {self.age}")

def create_random_person():
    names = ["Jordan", "Matan", "Gilad", "Koral", "Shahaf", "Ziv", "Maya"]
    id_numbers = [str(random.randint(100000000, 999999999)) for i in range(10)]
    ages = [random.randint(1, 100) for i in range(10)]
    name = random.choice(names)
    id_number = random.choice(id_numbers)
    age = random.choice(ages)
    return Person(name, id_number, age)

if __name__ == "__main__":
    people = []
    for i in range(10):
        person = create_random_person()
        people.append(person)

    for i, person in enumerate(people, 1):
        print(f"Person {i}:")
        person.print_info()
        print()

"""
Enums is a set of symbolic names bound to unique values. It can be iterated over to return its canonical members in definition order. 
It provides a way to create more readable and self-documenting code by using meaningful names instead of arbitrary values.

Some of the advantages of using enums include:
Readability and Self-Documentation: Enums provide meaningful names to values, making the code more human-readable and self-explanatory.
Reduced risk of errors: Enums help prevent the use of incorrect or inconsistent values in your code, reducing the risk of bugs and errors.
"""
