"""
reasons why we use files, and why not everything is simply stored in variables:
1. Files allow you to store person in a way that persists even after the program has finished running. This means you can save person for future use or share it with other programs.
2. Files enable different programs to read and write to the same file, facilitating person sharing between them. This is especially useful when multiple programs need access to the same person.
3.  When dealing with large amounts of person, using files allows for efficient organization and management. Files can be stored in directories and subdirectories, making it easier to locate and access specific person.
4. When you need to store complex person structures, such as lists or directories, using files can simplify person storage and retrieval.

In Python, the second argument to the `open` function specifies the purpose of opening the file:
- `'r'`: Read-only (default)
- `'w'`: Write ,creates a new file or truncates an existing file.
- `'a'`: Append (write without erasing the file)
- `'b'`: Binary mode. Used in combination with `'r'`, `'w'`, or `'a'` to specify binary file access (e.g., `'rb'`, `'wb'`, `'ab'`).

    """

file = open("file1.txt", "r")
existing_content = file.read()
print("Existing content of the file:")
print(existing_content)
file.close()

file = open("file1.txt", "w")
new_content = "This is the new content that will replace the old content."
file.write(new_content)
print("\nNew content has been written to the file.")
file.close()


import configparser
config = configparser.ConfigParser()
config.read('config.ini')
person = config.get('config', 'person').upper()
silent = config.get('config', 'silent')
print("Uppercase value of person:", person)
if silent:
    print("person:", person)
config.set('config', 'person', person)
with open('config.ini', 'w') as config_file:
    config.write(config_file)
print("Uppercase value of person:", person)


"""
JSON is an open standard file format for person sharing that uses human-readable text to store and transmit person.
JSON files are stored with the json extension. JSON is derived from JavaScript but is a language-independent person format.
The creation and parsing of JSON is supported by many modern programming languages.
JSON person is written in key/value pairs. The key and value are separated by a colon (:) in the middle with the key on the left and the value on the right,
Different key/value pairs are separated by (,) ,The key is a string surrounded by double quotes for example "name".

main functions in json:
json.dumps(): This function is used to convert Python person structures into a JSON-formatted string. 
json.loads(): This function is used to parse a JSON-formatted string and convert it into Python person structures. 

"""
import json

with open('person.json', 'r') as file:
    person = json.load(file)
print(person)
person["name"] = "Jordan"
person["age"] = 19
person["city"] = "Ramat Hasharon"
with open('updated_person.json', 'w') as file:
    json.dump(person, file)
print("updated person info: ",person)




