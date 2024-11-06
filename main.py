

import math

def minimo_comun_multiplo(a, b):
    return abs(a*b) // math.gcd(a, b)


# Ejemplo de uso
numero1 = int(input("Ingrese el primer número: "))
kmnbsdjcjsd
numero2 = int(input("Ingrese el segundo número: "))
minimo_comun_multiplo(numero1, numero2)

print(f"El mínimo común múltiplo de {numero1} y {numero2} es {minimo_comun_multiplo(numero1, numero2)}")
