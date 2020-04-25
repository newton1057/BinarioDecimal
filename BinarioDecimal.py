# Codigo para convertir un numero binario en Decimal, 
# consiste en el llenar una lista(array) con los digitos
# El numero binario debe ponerse de derecha a izquierda
# Ejemplo 16 en Binario es 10000, asi que en el programa debe ponerse 00001
# Autor: Eduardo Isaac Davila Bernal
# Fecha: 25/04/2020

def potencia(base,exponente):
    resultado = 1
    if exponente == 0:
        resultado = 1
    else:
        for i in range(exponente):
            resultado = resultado * base
    return resultado
    

numeroposicion = int(input("Cuantos Caracteres tiene tu numero Binario: "))

lista=[]

for k in range(numeroposicion):
    lista.append(int(input(f"Dame el valor de la posicion {k}: ")))

aux=0
decimal=0
for k in range(numeroposicion):
    aux=lista[k]
    if aux==1:
        decimal = decimal + potencia(2,k)
    
print(decimal)