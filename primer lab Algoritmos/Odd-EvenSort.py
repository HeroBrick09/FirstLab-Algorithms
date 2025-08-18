import random
import time

def main():
    inicio = time.time()
    A30, A100, A1000 = arrayGen(30), arrayGen(100), arrayGen(1000)
    n1, n2, n3 = len(A30), len(A100), len(A1000)
    print("Desordenado:")
    print(A)
    Ar = oddEvenSort(A,n)
    print("Ordenado:")
    print(Ar)
    fin = time.time()
    print(fin-inicio, "Segundos")

def oddEvenSort(a,n):
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

def arrayGen(n):
    array = []
    for i in range(n):
        num = random.randint(1,1001)
        array.append(num)
    return array

main()