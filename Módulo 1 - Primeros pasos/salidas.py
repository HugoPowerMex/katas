 # program.py
sum = 1 + 2
print(sum)

print('Hola desde la consola')

sum = 1 + 2 # 3
product = sum * 2
print(product)

 # fechas
from datetime import date
date.today()
print(date.today())
print("La fecha de hoy es: " + str(date.today()))

# input salida nombre
print("Bienvenido al programa de bienvenida")
name = input("Introduzca su nombre ")
print("Saludos: " + name)

# input salida numeros
print("Calculadora")
first_number = input("Primer número: ")
second_number = input("Segundo número: ")
print(first_number + second_number)

print(int(first_number) + int(second_number))
