def Palindrome(cadena):
	return cadena == cadena[::-1]
	
def Solucion(n):
	return Palindrome(bin(n)[2:]) and Palindrome(str(n))

def Main():
	j = 0
	for i in range(0, 10000001):
		if(Solucion(i)):
			j += 1
	print(j)

Main()