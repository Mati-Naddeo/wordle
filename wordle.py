import random
from threading import Timer
f = open("palabras.txt", "r")
lista = f.readlines()
f.close()

lista = [s[:-1] for s in lista]
palabraInput = ""
intentos = 0
palabra = (random.choice(lista))
print("La palabra tiene ", len(palabra), " letras." )
posIntentos = int(input("Ingrese la cantidad de intentos: "))
tiempo = int(input("Ingrese el tiempo: "))

def una_funcion():
    print("\nSe acabó el tiempo")
t = Timer(tiempo, una_funcion)
t.start()
while palabraInput != palabra and intentos < posIntentos:
    palabraInput = input("Ingrese una palabra: ").lower()
    i = 0
    espacio = ""
    while i < len(palabraInput):
        if palabraInput[i] ==  palabra[i]:
            espacio += "="
        elif palabraInput[i] in palabra:
            espacio += "-"
        elif palabraInput[i] not in palabra:
            espacio += " "
        i += 1
    print("",palabraInput, "\n",espacio)
    intentos += 1
else:
    if palabraInput == palabra:
        if intentos == 1:
            print("Correcto","\n", intentos," intento\n")

        else:
            print("Correcto","\n", intentos," intentos")
    elif  intentos >= posIntentos:
        print("Perdiste")
    else: 
        pass