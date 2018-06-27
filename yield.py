def combinations(iterable, k) :
	if k <= 0 or k > len(iterable) :
		yield []
		return
	yield from iterate(iterable, [], 1, -1, k) 
	

def iterate(iterable, accumulator, element, previous_i, k) :
	# recursion base, the kth element
	if element == k :
		for j in range(previous_i + 1, len(iterable)) :
			yield accumulator + [iterable[j]]
	else :
		for j in range(previous_i + 1, len(iterable) - (k-element)) :
			accumulator.append(iterable[j])
			yield from iterate(iterable, accumulator, element + 1, j, k)
			del accumulator[-1]

def potencia(lista):
	for i in range(0, len(lista)+1):
		yield from combinations(lista, i) 



for i in potencia(range(1,10)):
	print(i)