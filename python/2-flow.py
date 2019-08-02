#!/usr/bin/env python3

'''
Flow Control

Includes: Flow Control, Loop Constructs, Function Returns, Exceptions

Operators:
if, elif, else, while, return, raise, break, continue, for, try, except, finally
'''

def main():
	print('-----IF-----')
	ifDemo('Iron Man')
	ifDemo('Captain America')
	ifDemo('Ironman')

	print('-----WHILE-----')
	print(whileDemo(2,8))
	print(whileDemo(0,7))
	#print(whileDemo(7,1))

	print('-----BREAK-----')
	print(breakDemo(7))
	#breakDemo(-3)

	print('-----CONTINUE-----')
	continueDemo(10)

	print('-----FOR-----')
	print(forDemo([5, 4, 3, 5, 7]))
	forRangeDemo(0,10,1)
	
	print('-----EXCEPTION HANDLING-----')
	exceptionDemo()

def ifDemo(hero):
	if hero == 'Iron Man':
		print("I'm rich") 
	elif hero == 'Captain America':
		print('Suit up')
	else:
		print('Unknown hero')

def whileDemo(start, end):
	if start >= end:
		raise ValueError('Start can not be more or equal than end')

	while start < end:
		start += 1

	return start

def breakDemo(n):
	if n <= 0:
		raise ValueError('Number cannot be negative or zero')

	while True:
		print(n)
		n -= 1
		if n == 0:
			break

#Counts down only ODD numbers
def continueDemo(n):
	while n >= 0:
		if n % 2 == 0:
			n-=1
			continue
		else:
			print(n)
			n-=1
		print('I dont print for even')

def forDemo(numbers):
	total = 0
	for n in numbers:
		total += n

	return total

def forRangeDemo(start,end,step):
	#for(int i = start; i < end; i+=step)
	for i in range(start,end,step):
		#end is an optional paremeter
		#changes logic of function
		print(i, end=',')
	print()

def exceptionDemo():
	try:
		breakDemo(-5)
	except ValueError:
		print('breakDemo raised an error but was handled')
	finally:
		print('I will always execute')

if __name__ == '__main__':
	main()
