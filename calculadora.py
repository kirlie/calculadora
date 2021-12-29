print("Calculadora, elija una opción ingresando un número:")
print("1 - SUMA ")
print("2 - RESTA")
print("3 - MULTIPLICACION")
print("4 - DIVISION")

opcion = int(input("Elija la opcion"))

def suma(a, b):
    return (a + b)

def resta(a, b):
    return (a - b)
    
def multiplicacion(a, b):
    return (a * b)
    
def division(a, b):
    return (a // b)

if(opcion == 1):
    a = int(input("Ingrese el primer numero"))
    b = int(input("Ingrese el segundo numero"))
    print(suma(a, b))
elif(opcion == 2):
    a = int(input("Ingrese el primer numero"))
    b = int(input("Ingrese el segundo numero"))
    print(resta(a, b))
elif(opcion == 3):
    a = int(input("Ingrese el primer numero"))
    b = int(input("Ingrese el segundo numero"))
    print(multiplicacion(a, b))
elif(opcion == 4):
    a = int(input("Ingrese el primer numero"))
    b = int(input("Ingrese el segundo numero"))
    if (b == 0):
        print("No se puede dividir entre cero")
    print(division(a, b))
else:
    print("Elija una opcion entre 1 a 4")
