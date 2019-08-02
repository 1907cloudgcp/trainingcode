#!/usr/bin/env python3

'''
Strings, the array of characters.

- They are immutable (it's value in memory cannot change after
it is created)
- All string functions that look like they are changing the string
are returning you, a NEW string
- There is no char datatype in Python, so
python Strings are technically a List of Strings (of one character)

Includes: String Manipulation, String functions
'''

def main():
	#Concatenation
	print('Hello' + ' ' + 'String')

	normal = 'manipulate'
	upper = 'MANIPULATE'
	alpha_num = 'manipulate123456'
	numeric = '1232134512'
	case = 'mAnIpUlAtE' 

	#You can access them with an index
	print(normal[0])

	#Upper, Lower, Capitalize, Swap cases
	print(normal.upper())
	print(upper.lower())
	print(case.capitalize())
	print(case.swapcase())

	#Alpha-numeriqueness
	print(alpha_num.isalpha())
	print(alpha_num.isalnum())
	print(numeric.isnumeric())

	#Join a list by a delimiter
	strings = ['Welcome','to','the','string']
	delimiter = ':'
	joined = delimiter.join(strings)
	print(joined)

	#Split a string by a delimiter
	print(joined.split(':'))

	#Find first occurrence
	#index will raise an error if it doesn't exist
	#find will return -1
	print(normal.find('n'))
	print(normal.index('a'))

	#Length
	print(len(normal))

	#Location
	print(normal.startswith('m'))
	print(normal.endswith('e'))

	for s in normal:
		print(s, end=',')
		print(type(s))
	print()













	#We didn't change the structure, it's immutable!
	print(normal)

	


















if __name__ == '__main__':
	main()
