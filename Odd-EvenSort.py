import random
import time


def main():
    runSortsNoPrint()

def oddEvenSortHuman(a,n):
    is_sorted=False

    while not is_sorted:
        is_sorted=True

        for i in range(1,n-2,2):
            if a[i] > a[i+1]:
                a[i], a[i+1] = a[i+1], a[i]
                is_sorted = False
        for i in range(0,n-1,2):
            if a[i] > a[i+1]:
                a[i], a[i+1] = a[i+1], a[i]
                is_sorted = False
    return a

def odd_even_sort_ChatGpt(A, n):
    """
    Optimized Brick (Odd-Even) Sort algorithm.
    Sorts array A of size n in-place.
    """
    is_sorted = False
    while not is_sorted:
        is_sorted = True

        # Odd indexed pass
        for i in range(1, n - 1, 2):
            if A[i] > A[i + 1]:
                A[i], A[i + 1] = A[i + 1], A[i]
                is_sorted = False

        # Even indexed pass
        for i in range(0, n - 1, 2):
            if A[i] > A[i + 1]:
                A[i], A[i + 1] = A[i + 1], A[i]
                is_sorted = False
    return A

def odd_even_sort_Gemini(A, n):
    """
    Implementación optimizada del algoritmo Odd-Even Sort.

    Parámetros:
    A (list): La lista de números a ordenar.
    n (int): El tamaño de la lista.
    """
    is_sorted = False  # Bandera para controlar si el arreglo ya está ordenado
    while not is_sorted:
        is_sorted = True
        
        # Fase impar: compara elementos en posiciones impares con su siguiente
        # (A[1] con A[2], A[3] con A[4], ...)
        for i in range(1, n - 1, 2):
            if A[i] > A[i + 1]:
                A[i], A[i + 1] = A[i + 1], A[i]  # Intercambio
                is_sorted = False  # Si hubo un intercambio, el arreglo aún no estaba ordenado
                
        # Fase par: compara elementos en posiciones pares con su siguiente
        # (A[0] con A[1], A[2] con A[3], ...)
        for i in range(0, n - 1, 2):
            if A[i] > A[i + 1]:
                A[i], A[i + 1] = A[i + 1], A[i]  # Intercambio
                is_sorted = False  # Si hubo un intercambio, el arreglo aún no estaba ordenado
    
    return A

def odd_even_sort_blackbox(A, n):
    # Bandera para verificar si se realizaron intercambios
    sorted = False
    while not sorted:
        sorted = True
        
        # Fase impar
        for i in range(1, n, 2):
            if i < n - 1 and A[i] > A[i + 1]:
                A[i], A[i + 1] = A[i + 1], A[i]  # Intercambio
                sorted = False
        # Fase par
        for i in range(0, n, 2):
            if i < n - 1 and A[i] > A[i + 1]:
                A[i], A[i + 1] = A[i + 1], A[i]  # Intercambio
                sorted = False
    return A

def arrayGen(n):
    array = []
    for i in range(n):
        num = random.randint(1,1000)
        array.append(num)
    return array

def runSortsNoPrint():
    M1 = " brick sort algorithm Time Results:\n"
    M2 = "Size 30 array average sort time was: "
    M3 = "Size 100 array average sort time was: "
    M4 = "Size 1000 array average sort time was: "
    M5 = "Seconds"
    A10, A100, A1000 = arrayGen(30), arrayGen(100), arrayGen(1000)
    n1, n2, n3 = len(A10), len(A100), len(A1000)
    inicio30C, inicio100C, inicio1000C = [], [], []
    inicio30G, inicio100G, inicio1000G = [], [], []
    inicio30B, inicio100B, inicio1000B = [], [], []
    inicio30H, inicio100H, inicio1000H = [], [], []
    fin30C, fin100C, fin1000C = [], [], []
    fin30G, fin100G, fin1000G = [], [], []
    fin30B, fin100B, fin1000B = [], [], []
    fin30H, fin100H, fin1000H = [], [], []

    for i in range(5):
        inicio30C.append(time.perf_counter())
        odd_even_sort_ChatGpt(A10,n1)
        fin30C.append(time.perf_counter())

        inicio30G.append(time.perf_counter())
        odd_even_sort_ChatGpt(A10,n1)
        fin30G.append(time.perf_counter())

        inicio30B.append(time.perf_counter())
        odd_even_sort_ChatGpt(A10,n1)
        fin30B.append(time.perf_counter())

        inicio30H.append(time.perf_counter())
        odd_even_sort_ChatGpt(A10,n1)
        fin30H.append(time.perf_counter())

    for i in range(5):
        inicio100C.append(time.perf_counter())
        odd_even_sort_ChatGpt(A100,n2)
        fin100C.append(time.perf_counter())

        inicio100G.append(time.perf_counter())
        odd_even_sort_ChatGpt(A100,n2)
        fin100G.append(time.perf_counter())

        inicio100B.append(time.perf_counter())
        odd_even_sort_ChatGpt(A100,n2)
        fin100B.append(time.perf_counter())

        inicio100H.append(time.perf_counter())
        odd_even_sort_ChatGpt(A100,n2)
        fin100H.append(time.perf_counter())
    
    for i in range(5):
        inicio1000C.append(time.perf_counter())
        odd_even_sort_ChatGpt(A1000,n3)
        fin1000C.append(time.perf_counter())

        inicio1000G.append(time.perf_counter())
        odd_even_sort_ChatGpt(A1000,n3)
        fin1000G.append(time.perf_counter())

        inicio1000B.append(time.perf_counter())
        odd_even_sort_ChatGpt(A1000,n3)
        fin1000B.append(time.perf_counter())

        inicio1000H.append(time.perf_counter())
        odd_even_sort_ChatGpt(A1000,n3)
        fin1000H.append(time.perf_counter())
    
    print("\nChatGPT", M1)
    print(M2, averageTime(inicio30C, fin30C), M5)
    print(M3, averageTime(inicio100C, fin100C), M5)
    print(M4, averageTime(inicio1000C, fin1000C), M5)
    print("\nGemini", M1)
    print(M2, averageTime(inicio30G, fin30G), M5)
    print(M3, averageTime(inicio100G, fin100G), M5)
    print(M4, averageTime(inicio1000G, fin1000G), M5)
    print("\nBlackbox", M1)
    print(M2, averageTime(inicio30B, fin30B), M5)
    print(M3, averageTime(inicio100B, fin100B), M5)
    print(M4, averageTime(inicio1000B, fin1000B), M5)
    print("\nHuman", M1)
    print(M2, averageTime(inicio30H, fin30H), M5)
    print(M3, averageTime(inicio100H, fin100H), M5)
    print(M4, averageTime(inicio1000H, fin1000H), M5)

def averageTime(startTimes, endTimes):
    total = 0
    for i in range(len(startTimes)):
        total += endTimes[i] - startTimes[i]
    return total / len(startTimes)

main()