[+] Python - Classes and Objects [+]
-----------------------------------------------
things learnt - [1] object oriented programming
       	      	[2] classes
		[3] objects
		    [a] attributes
		    [b] methods
		    [c]properties
		 [i] data abstraction
		 [ii] data encapsulation
-------------------------------------------------------
[+]----------------Tasks----------------------[+]

0. My first square
   ~0-square.py: Python class Square that defines a square.

1.Square with size

  ~1-square.py: Python class Square that defines a square. Builds on 0-square.py with:
  		- Private instance attribute size.
		- Instantiation with size.
2. Size validation

   ~2-square.py: Python class Square that defines a square. Builds on 1-square.py with:
   		 -Instantiation with optional size: def __init__(self, size=0):
		 -If a provided size attribute is not an integer, a TypeError exception is raised with the message must be an integer.
		 -If a provided size attribute is less than 0, a ValueError exception is raised with the message size must be >= 0.
3. Area of a square

   ~3-square.py: Python class Square that defines a square. Builds on 2-square.py with:
   		 -Public instance attribute def area(self): that returns the current square area.
4. Access and update private attribute

   ~4-square.py: Python class Square that defines a square. Builds on 3-square.py with:
   		 -Property def size(self): to retrieve the private instance attribute self.
		 -Property setter def size(self, value): to set self.