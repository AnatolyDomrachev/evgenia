'''
Create a new string by deleting the middle k symbols from the original one. If the entered value of
k does not divide the string into two equal halves, make the left half smaller than the right one by one
symbol:
'''
def enter_data():
	st = input('Enter string: ')
	k = int(input('Enter k: '))
	return st, k 

def test_data(st,k):
	if k <= 0 or k >= len(st):
		raise Exception('Matrix not square!')

def ns_1(st,k,razn):
	ns = ''

	i = 0
	while i<razn/2 :
		ns += st[i]
		i+=1

	i = razn/2+k
	while i<len(st) :
		ns += st[int(i)]
		i+=1

	return ns

def ns_2(st,k,razn):
	ns = ''

	i = 0
	while i<razn/2-1 :
		ns += st[i]
		i+=1

	i = razn/2+k
	while i<len(st) :
		ns += st[int(i)]
		i+=1

	return ns

def new_string(st,k):
	razn = len(st) - k
	if razn % 2 == 0:
		ns = ns_1(st,k,razn)
	else:
		ns = ns_2(st,k,razn)
	return ns

st,k = enter_data() 
test_data(st,k)
print('Resulting string: ', new_string(st,k))


