import sys

print("Herramienta para calcular promedio (usar valores no decimales.)" )

n1 = int(input("Primera nota: "))
n2 = int(input("Segunda nota: "))
n3 = int(input("Tercera nota (dejar en cero si no existe): "))
n4 = int(input("Cuarta nota (dejar en cero si no existe): "))
n5 = int(input("Quinta nota (dejar en cero si no existe): "))
n6 = int(input("Sexta nota (dejar en cero si no existe): "))
n7 = int(input("Número de notas: "))

try: 
    result= (n1+n2+n3+n4+n5+n6)/n7

except ValueError as e:
    print("No se pueden usar números decimales, ni negativos")

except ZeroDivisionError:
    print("Error: No se puede dividir entre cero.")
    sys.exit(1)

print(f"Tu promedio es {result}")