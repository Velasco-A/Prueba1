

import math

def minimo_comun_multiplo(a, b):
    return abs(a*b) // math.gcd(a, b)


# Ejemplo de uso
numero1 = int(input("Ingrese el primer número: "))
numero2 = int(input("Ingrese el segundo número: "))
minimo_comun_multiplo(numero1, numero2)

print(f"El mínimo común múltiplo de {numero1} y {numero2} es {minimo_comun_multiplo(numero1, numero2)}")

def menu():
    print("Seleccione una operación:")
    print("1. Mínimo Común Múltiplo")
    print("2. Factorial")
    print("3. División")
    opcion = int(input("Ingrese el número de la operación deseada: "))
    return opcion

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

def division(a, b):
    if b == 0:
        return "Error: División por cero"
    else:
        return a / b

opcion = menu()

if opcion == 1:
    numero1 = int(input("Ingrese el primer número: "))
    numero2 = int(input("Ingrese el segundo número: "))
    resultado = minimo_comun_multiplo(numero1, numero2)
    print(f"El mínimo común múltiplo de {numero1} y {numero2} es {resultado}")
elif opcion == 2:
    numero = int(input("Ingrese un número: "))
    resultado = factorial(numero)
    print(f"El factorial de {numero} es {resultado}")
elif opcion == 3:
    numero1 = int(input("Ingrese el numerador: "))
    numero2 = int(input("Ingrese el denominador: "))
    resultado = division(numero1, numero2)
    print(f"El resultado de la división de {numero1} entre {numero2} es {resultado}")
else:
    print("Opción no válida")