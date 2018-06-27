#numero de palabras del cuento  N (2 ≤ N ≤ 1000)
#numero de lineas por pagina L (1 ≤ L ≤ 30)
#numero de caracteres por linea
import fileinput
import math

def numero_pag(limita, story):
    entradas = limita.split()
    letras = int(entradas[0])
    lineas = int(entradas[1])
    caracteres = int(entradas[2])
        
    L = 0
    C = 0
    N = story.split()
    for i in range(letras):
        if i == 0:
            C = len(N[i])
            L += 1
        else:
            C += 1 + len(N[i])
            if C > caracteres:
                C = len(N[i])
                L += 1
    pages = math.ceil(L / lineas)
    return pages


e = list()
for line in fileinput.input():
    e.append(line)

for i in range(0, len(e), 2):
    num = e[i]
    texto = e[i + 1]
    print(numero_pag(num, texto))

#Salida el numero de paginas minimas del cuento 