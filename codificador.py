
def codificador(l,opcion):
	abc = "abcdefghijklmnopqrstuvwxyz"
	codificador = "cdefghijklmnopqrstuvwxyzab"
	if opcion == "1":
		re = (l.translate({ord(x): y for(x,y) in zip(abc, codificador)}))
	if opcion == "2":
		re = (l.translate({ord(x): y for(x,y) in zip(codificador, abc)}))
	return re

while True:
	print("\tEste es un codificador y descodificador cesar. Escribe la opción que te interece\n")
	print("\t1.- Anota \"1\" si quieres codificar una palabra u oración\n")
	print("\t2.- Anota \"2\" si quieres descodificar una palabra u oración\n")
	print("\t\"exit\" para salir")
	opcion = input()
	if opcion == "1":
		print("Anota la palabra u oración que quieres codificar:")
		palabra = input()
		print("Ya esta codificado:")
		print(codificador(palabra, opcion))
	if opcion == "2":
		print("Anota la palabra u oración que quieres descodificar:")
		palabra = input()
		print("Ya esta descodificado:")
		print(codificador(palabra, opcion))
	if opcion == "exit":
		break

