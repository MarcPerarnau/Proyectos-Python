# Pedir números (acepta enteros y decimales)
numero1 = float(input("Introduce el primer número: "))
numero2 = float(input("Introduce el segundo número: "))

# Mostrar opciones
print("1. Sumar")
print("2. Restar")
print("3. Multiplicar")
print("4. Dividir")
escoger = int(input("¿Qué operación quieres ejecutar?: "))

# Operaciones
if escoger == 1:
    resultado = numero1 + numero2
    print(f"El resultado de la suma entre {numero1} y {numero2} es {resultado}.")
elif escoger == 2:
    resultado = numero1 - numero2
    print(f"El resultado de la resta entre {numero1} y {numero2} es {resultado}.")
elif escoger == 3:
    resultado = numero1 * numero2
    print(f"El resultado de la multiplicación entre {numero1} y {numero2} es {resultado}.")
elif escoger == 4:
    if numero2 == 0:
        print("No se puede dividir entre 0.")
    else:
        resultado = numero1 / numero2
        print(f"El resultado de la división entre {numero1} y {numero2} es {resultado}.")
else:
    print("Opción no válida.")
