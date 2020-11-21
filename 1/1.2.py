'''
Generate a random list of integer numbers. Number of elements and the generation range should be
requested from the user. Print the generated list on the screen. Without using insertion or deletion,
make a circular shift of all elements 1 step to the right, then print the modiϐied list.
'''

import random

def gen_list():
	size = int(input('list size: '))
	fist_rand = int(input('list fist_rand: '))
	last_rand = int(input('list last_rand: '))
	data=[]
	i=0
	while i<size:
		data.append(random.randint(fist_rand,last_rand))
		i+=1

	return data

def sdvig(array):
	size = len(array)-1
	new_array = array[size:] + array[:size]
	return new_array


# Generate a random list of integer numbers
array = gen_list()
new_array = sdvig(array)
print(array)
print(new_array)
