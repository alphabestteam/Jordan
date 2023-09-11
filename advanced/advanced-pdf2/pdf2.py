"""
*args allows a function to take an unlimited number of arguments in tuple form.
When a function uses *args by definition, it allows you to pass an irregular amount of arguments to the function and use them as if they were stored inside a tuple within the function.

**kwargs allows the function to take an unlimited number of arguments in dictionary form.
When a function uses **kwargs** by definition, it allows you to pass an irregular amount of arguments to the function and use them as if they were stored in a dictionary within the function, where the keys that help you access dictionary entries are the names you use when calling the function.

The differences between *args and **kwargs* are that *args allows you to accept an unlimited number of arguments and access them as if they were in a tuple.
**kwargs allows you to accept an unlimited number of arguments and access them as if they were in a dictionary.
 Both concepts can be used together when you want to create a function that allows you to pass 
an unlimited number of arguments and also pass variables in the form of a tuple and a dictionary.

Packing:
This is where we enter several variables into a data structure (tuple ,list, dictionary).
By wrapping the variables together, we create a single data structure in which the variables can be stored and transferred together.

Unpacking:
This is where we break down data structures and get the values inside them into separate variables.
"""
#example for packing:
my_data = ("jordan", 19, "tlv")
#example for unpacking:
name, age, city = ("jordan", 19, "tlv")

def words_length(*words):
    total_length = 0
    for word in words:
        total_length += len(word)
    print(f'total_length: {total_length}')


def total_age(**ages):
    total_ages = 0
    for name, age in ages.items():
        print(f"{name}: {age} ")
        total_ages += age
    print(f'total ages is {total_ages}')

words_length("hello", "i", "am", "jordan")
total_age(age1=19, age2=23, age3=44)  

