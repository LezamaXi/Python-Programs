from sys import stdin

def producto_cruz(l1, l2):
	return(l1[0] * l2[1] - l1[1] * l2[0])

def resta(x1, y1, x2, y2):
	return (x2-x1, y2-y1)

def signo_valido(l, p):
	if producto_cruz(l, p) > 0:
		return True
	return False

def punto_interno(x1, y1, x2, y2, x3, y3, x4, y4):
	l1 = resta(x2, y2, x1, y1)
	l2 = resta(x2, y2, x3, y3)
	l3 = resta(x1, y1, x3, y3)
	p4 = (x4, y4)
	signos = [signo_valido(l1, p4), signo_valido(l2, p4), signo_valido(l3, p4)]
	print(signos)
	if( signos == [False, False, False]):
		return True
	else: return False

interno = 0
externo = 0
for x in stdin :
	linea = x.split()
	if linea == [] :
		break
	x1, y1, x2, y2, x3, y3, x4, y4= map(int, linea)
	if punto_interno(x1, y1, x2, y2, x3, y3, x4, y4) :
		interno += 1
	else: 
		externo += 1

print(interno)
print(externo)




