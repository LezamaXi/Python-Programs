from sys import stdin

def lucky(a, b):
	j = 0
	for x in range(a,b+1):
		num = set()
		dij = str(x)
		for c in dij:
			num.add(c)
		if(len(num) == len(dij)):
			j+= 1
	return j
for x in stdin:
	a,b = map(int, x.split())
	print(str(lucky(a,b)))