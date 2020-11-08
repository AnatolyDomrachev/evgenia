'''
Task 2.1
Request a matrix of integer numbers from the user and make sure it is a square one (number of rows =
number of columns).
Print the matrix on the screen.
Find the sum of numbers on the main diagonal and on the antidiagonal.
'''

import math

def test_sqare_matrix(array):
	sqr = math.sqrt(len(array))
	return int(sqr) == sqr

def get_matrix():
	string = input('enter matrix as space separated string: ')
	array = string.split();
	if(not test_sqare_matrix(array)):
		raise Exception('Matrix not square!')
	size = math.sqrt(len(array))
	matrix=[]
	i=0
	while i<size:
		matrix.append([])
		j=0
		while j<size:
			matrix[i].append(int(array[int(size)*i + j]))
			j+=1
		i+=1
	
	return matrix

def sum_diag(matrix):
	size = len(matrix)
	i=0
	sd = 0
	while i<size:
		sd += matrix[i][i]
		i+=1
	return sd

def sum_a_diag(matrix):
	size = len(matrix)
	i=0
	sd = 0
	while i<size:
		sd += matrix[size-i-1][i]
		i+=1
	return sd

def put_matrix():
	size = len(matrix)
	i=0
	while i<size:
		j=0
		print()
		while j<size:
			print(matrix[i][j], end=' ')
			j+=1
		i+=1
	print()

matrix = get_matrix()
put_matrix()
sd = sum_diag(matrix)
print('Sum of the main diagonal: ', sd)
sad = sum_a_diag(matrix)
print('Sum of the antidiagonal: ', sad)

