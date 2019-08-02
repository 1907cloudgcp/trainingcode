#!/usr/bin/env python3

'''
Functions

Includes: Built-in functions, Functional Programming, Lambdas
'''

#GLOBAL SCOPE
#Accessible by all functions
globalValue = 3.141592

def main():
	### BUILT IN FUNCTIONS ###
	
	#Do not forget 
	print(print)
	
	#Transformation functions (not casting but it does that)
	
	#To Int
	print(int(5.7))
	print(int('5'))

	#To Float
	print(float(5))

	#To String
	print(str([1,2,3]))
	print(str(3.141592))

	#To Tuple
	print(tuple([1,2,3]))
	
	#To List
	print(list({1,2,4}))

	#To Set	
	print(set([1,2,2,2,2,2,4,90387642,1234522]))

	#Mathematical
	numbers = [-132, 6, 7, 9000, 34, -143]

	#Mininum
	print(min(numbers))

	#Maximum
	print(max(numbers))
	
	#Length
	print(len(numbers))

	#Magnitude
	print(abs(-9))

	#Power (but we have **???)
	print(pow(2,10))

	#Round (it rounds up, but we have //???)
	print(round(3.57, 1))
	print(round(3.57,0))
	#???
	print(round(3.55,1))
	print(round(3.65,1))
	print(round(3.675,2))	
	
	#Sort (ascending or descending)
	print(sorted(numbers))
	print(sorted(numbers, reverse=True))

	boolGroup = [True, 5.0, True, 0, '7']
	
	#All true
	print(all(boolGroup))

	#At least one is true
	print(any(boolGroup))

	variable = 7
	print(eval('variable + 3'))

	#Range
	print(range(0,10,2))	

	#LOCAL SCOPE (FUNCTION SCOPE)
	localValue = 'local'
	
	#This works
	print(globalValue)

	#???
	#There is no BLOCK scope
	if True:
		x = 7
	print(x)

	#Anonymous functions
	#SUM
	print(calculate(7,5, lambda x,y: x + y))

	#SUB (not anonymous)
	print(calculate(7,5,substraction))


#Functional Programming
def calculate(x, y, operator):
	#Executing call-back function
	#(function that may or may not be executed later)
	return operator(x,y)

def substraction(x, y):
	return x - y

#This works
print(globalValue)

#This breaks
#print(localValue)


if __name__ == '__main__':
	main()
