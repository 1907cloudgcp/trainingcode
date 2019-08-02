#!/usr/bin/env python3

'''
Python Basics

Includes: Operands, Data Types, and Variables
'''

#Main function always has to be first
def main():
	print('Python Basics')
	
	### OPERATORS ###
	
	#Arithmetic Operators

	#+,-,/,*,%
	print(5 + 7)
	print(4 % 2)
	
	#Floored Quotient
	print(20 // 8)

	#Operand Order (Left to Right, ADD/SUB first, PROD/DIV second)
	print((4 - 1) * ((3 + 2)/(8 - 3)))

	#Reassign a variable to a different type
	x = '5'
	x = 5

	#Negate
	print(-x)

	#Power
	print(2 ** 32)

	#Relational Operators
	
	#<,<=,>,>=,==,!=
	print(2 < 3)
	print(2 != 3)
	print(3 == 3)

	#Boolean Operators

	print(True or False)
	print(True and True)
	print(not False)

	### Data types ###
	
	#NUMBERS
	
	#(int)
	#In python 3 there is no long anymore
	#int can hold any size of number, considering your memory.
	integer = 1 + 3
	print(type(integer))

	#(float)
	floating = 3 / 4
	floating = 1.0
	print(type(floating))

	#(complex)
	complexN = 3.14J
	print(type(complexN))

	#BOOLEAN

	#(bool)
	boolean = True
	print(type(boolean))

	#(string)
	string = 'String'
	string += 'Another'
	print(type(string))

	#DATA STRUCTURES
	
	#(list)
	empty = []
	regular = [1, 2, 4, 3, 3, 3]
	mixed = [1, '5', True, 'hello', 5.0]
	print(regular)
	print(type(regular))

	#(set)
	emptySet = {}
	regularSet = {1, 5, 5, 6, 6, 9, 0}
	print(regularSet)
	print(type(regularSet))

	#(tuple)
	emptyTuple = ()
	regularTuple = (1, 2, 3, 3, 5)
	print(regularTuple)
	print(type(regularTuple))

	#(dict)
	#{Key:Value, Key:Value, ...}
	#Similar to JSON
	#Similar to Map in Java
	dictionary = {'pedro':27, 'bob':45, 'bobbert':48}
	print(dictionary)
	print(type(dictionary))
	
	#(None)
	#This gets returned by functions that don't (void)
	#This is technically null in Python
	none = None
	print(type(none))

	#(function)
	function = myFunction
	function(5)
	print(type(function))

def myFunction(number):
	print('Value: ' + str(number))

'''
This is how you invoke the main() function
When python strats, it will create the __name__ variable
with a value of __main__.

When the script is imported, this will have a different value
and won't execute our logic.
'''
if __name__ == '__main__':
	main()
