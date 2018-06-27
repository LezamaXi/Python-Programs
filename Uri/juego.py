def suma(lista):
	lis = lista
	m = []
	if(len(lis)/2 == 0):
		i = 0
		for x in range(len(lis)):
			su = lis[i] + lis[x]
			i += 1
			m.append(su)
	else:
		for x in range(len(lis)-1):
			su = lis[i] + lis[x]
			i += 1
			m.append(su)
	return m

def resta(lista):
	lis = lista
	m = []
	if(len(lis)/2 == 0):
		i = 0
		for x in range(len(lis)):
			su = lis[i] + lis[x]
			i += 1
			m.append(su)
	else:
		for x in range(len(lis)-1):
			su = lis[i] + lis[x]
			i += 1
			m.append(su)
	return m

def secuencia(lista, incio):
	aux = int(len(lista))
	respaldo = lista
	m = respaldo
	while(aux == 0):
		print(aux)
		if(inicio == 0):
			#Empieza Rusa, Rusa es 0
			m = suma(m)
			m = resta(m)
			if(len(m) == 1 and int(m)/2 == 0):
				return m
				print(m)
			else: 
				return m
				print(m)
		elif(inicio == 1):
			#Empieza Sanches
			m = suma(m)
			m = resta(m)
			if(len(m) == 1 and int(m)/2 == 0):
				return m
				print(m)
			else: 
				return m
				print(m)
		aux = int(aux/2)
Sanches = 1
Rusa = 0
lista  = [4, 2, 3, 5, 1, 6, 10, 2]
print(lista)
resutado = secuencia(lista, Sanches)
print(resutado)





