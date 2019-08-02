#!/usr/bin/env python3

'''
Collections
'''

def main():
	#List
	'''
	- They are ordered (they keep order of instertion)
	- They can hold duplicates
	- It is technically the "array" of Python
	'''
	my_list = [1,2,4,9,34,-5,9,9,9]
	print('List: ' + str(my_list))

	#Set
	'''
	- They are NOT ordered (order of insertion is not guaranteed)
	- They only hold unique values
	'''
	my_set = {1,4,5,7,7,7,9,87,898598595,-9347934,42,34}
	print('Set: ' + str(my_set))	

	#Tuple
	'''
	- It's the list direct sibling
	- It is read-only, and performs faster for read operations
	'''
	my_tuple = (1,2,4,5,6,6,7,8)
	print('Tuple: ' + str(my_tuple))
	
	#Splicing
	print(my_list[:3])
	print(my_list[-3:])
	print(my_list[2:4])

	#Set Operators
	setA = {5,7,4,8}
	print('Set A' + str(setA))
	setB = {1,2,4,8}
	print('Set B' + str(setB))

	print(setA | setB)
	print(setA & setB)
	print(setA - setB)
	print(setB - setA)

	#Dictionary
	mapDemo = {'pedro':54J, 'peter':139, 'bobbert':954}

	print(mapDemo['pedro'])

	mapDemo['another'] = 5

	for key in mapDemo.keys():
		print(mapDemo[key])
	
	print(mapDemo.items())











if __name__ == '__main__':
	main()
