def array_sum(arr):
    """Devuelve la suma de todos los elementos en un array (lista)."""
    total = 0
    for num in arr:
        total += num
    return total


if __name__ == "__main__":
    # Ejemplo de uso
    numeros = [1, 2, 3, 4, 5]
    print("Array:", numeros)
    print("Suma de elementos:", array_sum(numeros))
