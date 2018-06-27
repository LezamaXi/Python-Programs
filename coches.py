from IPython.display import clear_output # Se necesita para limpiar la salida del notebook
import time # Se necesita para dormir el programa
import random # Se necesita para obtener la distancia aleatoria a avanzar

participantes = [] # Lista de los participantes de la carrera
distancia_de_meta = 140 # Tamaño de la pista de carreras en metros

class Vehiculo:
    tam_tanque = 0 # Tamaño del tanque de gasolina
    min_distancia = 0 # Cantidad máxima de metros que puede avanzar un carro en una iteración
    max_distancia = 0 # Cantidad mínima de metros que puede avanzar un carro en una iteración
    distancia_recorrida = 0 # Distancia recorrida por el vehículo
    refil = tam_tanque #Rellena el tanque a su maxima capacidad

    
    def __init__(self):
        """Inicializa la clase padre del vehículo"""
        self.tanque = self.tam_tanque # Llena el tanque del vehículo
    
    def avanzar():
        """
        Avanza el vehículo una cantidad aleatoria entre
        su distancia mínima y máxima reduciendo 1 unidad
        en su tanque de gasolina. Si este se encuentra vacio
        entonces el vehículo no avanza pero rellena su tanque.
        Si el vehículo ha llegado a la meta este ya no avanza.
        """
        
 

class Moto(Vehiculo):
    tam_tanque = 5
    min_distancia = 4 
    max_distancia = 6 
    distancia_recorrida = 0

    def __init__(self):
        super().__init__()

    def avanza(self):
        if (self.tanque == 0):
            self.tanque = self.tam_tanque
        else:
            self.distancia_recorrida += random.randint(self.min_distancia, self.max_distancia)
            self.tanque -= 1
    
class Coche(Vehiculo):
    tam_tanque = 7
    min_distancia = 3 
    max_distancia = 9
    distancia_recorrida = 0

    def __init__(self):
        super().__init__()

    def avanza(self):
        if (self.tanque == 0):
            self.tanque = self.tam_tanque
        else:
            self.distancia_recorrida += random.randint(self.min_distancia, self.max_distancia)
            self.tanque -= 1
    
class Avion(Vehiculo):
    tam_tanque = 6
    min_distancia = 5 
    max_distancia = 8
    distancia_recorrida = 0

    def __init__(self):
        super().__init__()

    def avanza(self):
        if (self.tanque == 0):
            self.tanque = self.tam_tanque
        else:
            self.distancia_recorrida += random.randint(self.min_distancia, self.max_distancia)
            self.tanque -= 1

class Bici(Vehiculo):
    tam_tanque = 7
    min_distancia = 6 
    max_distancia = 9
    distancia_recorrida = 0

    def __init__(self):
        super().__init__()

    def avanza(self):
        if (self.tanque == 0):
            self.tanque = self.tam_tanque
        else:
            self.distancia_recorrida += random.randint(self.min_distancia, self.max_distancia)
            self.tanque -= 1
    
def imprime_carrera():
    """Imprime el estado de la carrera"""
    len_pista = 160 # Longitud en ascii del circuito de carreras
    pistas = ""
    for x in range(len(participantes)): # Itera sobre los vehículos
        vehiculo = participantes[x]
        pista = "-"*len_pista
        posicion = (vehiculo.distancia_recorrida * len_pista) // distancia_de_meta
        posicion = min(len_pista,posicion)
        pista = pista[:posicion] + "*" + pista[posicion:]
        pistas += '\n{:2d} '.format(x) + pista
    clear_output(wait=True)
    print(pistas)
        

def juego_terminado():
    for v in participantes:
        if(v.distancia_recorrida >= distancia_de_meta):
            return True
    return False

def avanza_carrera():
    for i in participantes:
            i.avanza()

def inicializa_participantes(x):
        if x == 1:
            participantes.append(Moto())
        elif x == 2:
            participantes.append(Coche())
        elif x == 3:
            participantes.append(Avion())
        elif x == 4:
            participantes.append(Bici())

def main():
    print("Juego comenzado.")
    print("¿Cuantos participantes quieres poner a competir?")
    concursantes = input()
    print("Escoje tus concursantes y escribe su numero")
    print(str.format( "1 Moto\n"
                      "2 Coche\n"
                      "3 Avion\n"
                      "4 Bici"))
    
    for i in range(int(concursantes)):
        inicializa_participantes(int(input()))

    imprime_carrera()    
    while not juego_terminado():
        imprime_carrera()
        time.sleep(1)
        avanza_carrera()

    imprime_carrera()
        # Se encarga de dormir el programa un segundo
    print("Juego terminado.")

main()