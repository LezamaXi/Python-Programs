def valido(n) :
	cad = str(n)
	dic = {}
	for c in cad :
		if c in dic :
			return False
		else :
			dic[c] = 1
	return True

def neutro(n) :
	cad = str(n)
	creciente = False
	if len(cad) < 3 :
		return False

	if cad[0] < cad[1] :
		creciente = True
	
	for i in range(1, len(cad)-1) :
		if creciente and cad[i] > cad[i+1] :
			return True
		if not creciente and cad[i] < cad[i+1] :
			return True
	return False

def solucion():
	total = 1
	neutros = 0 
	z = 1
	while(neutros/total < 0.9) :
		if valido(z) :
			total += 1
			if neutro(z) :
				neutros+= 1
		z += 1
	return z-1

print(str(solucion()))
