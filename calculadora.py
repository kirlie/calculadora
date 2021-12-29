print("Calculadora, elija una opción ingresando un número:")
print("1 - SUMA ")
print("2 - RESTA")
print("3 - MULTIPLICACION")
print("4 - DIVISION")

opcion = int(input("Elija la opcion"))

def suma(a, b):
    return (a + b)

if(opcion == 1):
    a = int(input("Ingrese el primer numero"))
    b = int(input("Ingrese el segundo numero"))
    print(suma(a, b))
elif(opcion == 2):
    print("opcion 2")
elif(opcion == 3):
    print("opcion 3")
elif(opcion == 4):
    print("opcion 4")
else:
    print("Elija una opcion entre 1 a 4")
