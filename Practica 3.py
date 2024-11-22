#Funcion de promedio
def promediar ():
    n=int(input("Ingresar cantidad de notas: "))
    suma=0
    for i in range (n):
        nota=float(input(f"Ingrese la {i+1}: "))
        suma +=nota
    promedio=suma/n
    return promedio
resultado=promediar()
print(f"El promedio de tus notas es: {resultado}")

#Color primario o no
def color_primario (color):
    colores_primarios=["rojo", "azul", "amarillo"]
    if color in colores_primarios:
        print(f"El color {color} es primario")
    else:
        print(f"El color {color} no es primario")
color= input("Ingrese un color: ").lower()
color_primario(color)

#¿Qué número es mayor?
def encontrar_mayor ():
    n=int(input("Ingrese la cantidad de números: "))
    mayor=float(input("Ingrese el número 1: "))
    for i in range (1, n):
        numero=float(input(f"Ingrese el número {i+1}: "))
        if numero>mayor:
            mayor=numero
    print(f"El número mayor es: {mayor}")
encontrar_mayor()

#Rectángulo
def dibujar_rectangulo (filas, columnas):
    for i in range (filas):
        print ("*"*columnas)
filas=int(input("Ingrese la cantidad de filas: "))
columnas= int(input("Ingrese la cantidad de columnas: "))
dibujar_rectangulo(filas, columnas)

#Factorial
def calcular_factorial (n):
    if n==0 or n==1:
        return 1
    else:
        return n*calcular_factorial(n-1)

numero=int(input("Ingrese un número entero positivo: "))
resultado=calcular_factorial(numero)
print(f"El factorial de {numero} es: {resultado}")