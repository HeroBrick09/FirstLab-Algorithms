import random
import time

def main():
    inicio = time.time()
    A = arrayGen(30)
    n = len(A)
    print("Desordenado:")
    print(A)
    Ar = odd_even_sort(A,n)
    print("Ordenado:")
    print(Ar)
    fin = time.time()
    print(fin-inicio, "Segundos")

def odd_even_sort(arr, n):
    is_sorted = False

    while not is_sorted:
        is_sorted = True

        # Fase impar (índices impares)
        for i in range(1, n - 1, 2):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                is_sorted = False

        # Fase par (índices pares)
        for i in range(0, n - 1, 2):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                is_sorted = False

    return arr

def arrayGen(n):
    array = []
    for i in range(n):
        num = random.randint(1,1001)
        array.append(num)
    return array

main()