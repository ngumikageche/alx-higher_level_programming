[+]Python - Input/Output[+]
Reading and Writing Files
-----------------------------------
open() returns a file object, and is most commonly used with two positional arguments and one keyword argument: open(filename, mode, encoding=None)
f = open('workfile', 'w', encoding="utf-8")
Warning Calling f.write() without using the with keyword or calling f.close() might result in the arguments of f.write() not being completely written to the disk, even if the program exits successfully
--------------------------
Saving structured data with json
------------------------------------------
Strings can easily be written to and read from a file. Numbers take a bit more effort, since the read() method only returns strings, which will have to be passed to a function like int(), which takes a string like '123' and returns its numeric value 123. When you want to save more complex data types like nested lists and dictionaries, parsing and serializing by hand becomes complicated.

Rather than having users constantly writing and debugging code to save complicated data types to files, Python allows you to use the popular data interchange format called JSON (JavaScript Object Notation). The standard module called json can take Python data hierarchies, and convert them to string representations; this process is called serializing. Reconstructing the data from the string representation is called deserializing. Between serializing and deserializing, the string representing the object may have been stored in a file or data, or sent over a network connection to some distant machine.
--------------------------
json.dump() in Python
Last Updated : 23 Jan, 2020
Read
Discuss
Courses
Practice
Video

The full-form of JSON is JavaScript Object Notation. It means that a script (executable) file which is made of text in a programming language, is used to store and transfer the data. Python supports JSON through a built-in package called json. To use this feature, we import the json package in Python script. The text in JSON is done through quoted-string which contains the value in key-value mapping within { }. It is similar to the dictionary in Python.

json.dump()
json module in Python module provides a method called dump() which converts the Python objects into appropriate json objects. It is a slight variant of dumps() method.

