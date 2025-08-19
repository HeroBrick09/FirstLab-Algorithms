import random
import time

def main():
    runSortsNoPrint()

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
        num = random.randint(1,1000)
        array.append(num)
    return array

def runSorts():
    A10, A100, A1000 = arrayGen(30), arrayGen(100), arrayGen(1000)
    n1, n2, n3 = len(A10), len(A100), len(A1000)

    print("Odd-Even Sort Array size 30 \n disarranged array: \n", A10)
    inicio1 = time.perf_counter()
    ar30 = oddEvenSort(A10,n1)
    fin1 = time.perf_counter()
    print("sorted array: \n", ar30)

    print("Odd-Even Sort Array size 30 \n disarranged array: \n", A100)
    inicio2 = time.perf_counter()
    ar100 = oddEvenSort(A100,n2)
    fin2 = time.perf_counter()
    print("sorted array: \n", ar100)
    

    print("Odd-Even Sort Array size 30 \n disarranged array: \n", A1000)
    inicio3 = time.perf_counter()
    ar1000 = oddEvenSort(A1000,n3)
    fin3 = time.perf_counter()
    print("sorted array: \n", ar1000)
    

    print("Size 30 array was sorted in: ", fin1-inicio1, "Seconds")
    print("Size 100 array was sorted in: ", fin2-inicio2, "Seconds")
    print("Size 1000 array was sorted in: ", fin3-inicio3, "Seconds")

def runSortsNoPrint():
    A10, A100, A1000 = arrayGen(30), arrayGen(100), arrayGen(1000)
    n1, n2, n3 = len(A10), len(A100), len(A1000)
    inicio30, inicio100, inicio1000 = [], [], []
    fin30, fin100, fin1000 = [], [], []

    for i in range(5):
        inicio30.append(time.perf_counter())
        oddEvenSort(A10,n1)
        fin30.append(time.perf_counter())
    for i in range(5):
        inicio100.append(time.perf_counter())
        oddEvenSort(A100,n2)
        fin100.append(time.perf_counter())
    
    for i in range(5):
        inicio1000.append(time.perf_counter())
        oddEvenSort(A1000,n3)
        fin1000.append(time.perf_counter())
    

    print("Size 30 array average sort time was: ", averageTime(inicio30, fin30), "Seconds")
    print("Size 100 array average sort time was: ", averageTime(inicio100, fin100), "Seconds")
    print("Size 1000 array average sort time was: ", averageTime(inicio1000, fin1000), "Seconds")

def averageTime(startTimes, endTimes):
    total = 0
    for i in range(len(startTimes)):
        total += endTimes[i] - startTimes[i]
    return total / len(startTimes)
main()