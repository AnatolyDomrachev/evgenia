'''
In the program code, deϐine a dictionary of word translations from English into Russian. Input a sen‑
tence. Translate the sentence word by word using the deϐined dictionary. Words that don’t have trans‑
lations deϐined are kept without any change. The ϐinal resulting value should be a single string.
'''

def a_to_s(array):
	st = ''
	i=0 
	while(i<len(array)):
		st += array[i] + ' '
		i+=1
	return st

def translate(swap, string):
	array = string.split()

	i=0 
	while(i<len(array)):
		if swap.get(array[i]):
			array[i] = swap.get(array[i])
		i+=1
	return a_to_s(array)

swap = {'hello':'Привет','world':'мир'}
string = input('Enter string: ')
print(translate(swap, string))
