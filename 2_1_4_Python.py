import math

#Llamado por teclado para los numeros a calcular
primer_numero = int(input("Ingrese un numero: "))
segundo_numero = int(input("Ingrese un numero: "))

print("La suma de los numeros es: ", primer_numero + segundo_numero)
print("La resta de los numeros es: ", primer_numero - segundo_numero)
print("La multiplicacion es: ", primer_numero * segundo_numero)

if(segundo_numero == 0):
    print("No se puede dividir por 0")
else:
    print("La division es: ", primer_numero / segundo_numero)

raiz1= math.sqrt(primer_numero)
raiz2= math.sqrt(segundo_numero)

print(f"La raiz cuadrada del primer numero es {raiz1} y la raiz del segundo numero es {raiz2}")
print("La potencia es: ",primer_numero**segundo_numero)

nombre = input("¿Cual es su nombre?: ")
calificacion = float(input("Califique el programa con una nota: "))
descripcion=input("Describa el por que de su calificación: ")

print("¿Cual es su nombre?: ",nombre)
print("Califique el programa con una nota: ",calificacion)
print("Describa el por que de su calificación: ",descripcion)
