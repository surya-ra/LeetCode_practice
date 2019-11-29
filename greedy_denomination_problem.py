'''
This approach will fail in the following case
Let,
denom = [25, 10, 6, 5, 1]
value = 12

This algorithm will give the following result- 

value   ------------   denom
12      ------------   10
2       ------------   1
1       ------------   1

Hence output = [10, 1, 1] == 3 
But this can be done using 2 denomination of 6 (6 + 6)

Hence, the outpust given by the following algorithm is not optimal
in the above mentoned case.
'''
def findOptimalDenoms(val):
	#the denominations are sorted in decreasing order
	denom = [25, 10, 5, 1]
	iterate = 0
	op = []

	#find denominations till the value is greater than zero
	while val > 0:
		while val >= denom[iterate]:
			val -= denom[iterate]
			op.append(denom[iterate])
		iterate += 1
	print(op)

if __name__ == '__main__':
	findOptimalDenoms(11)