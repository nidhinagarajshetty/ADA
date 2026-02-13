import random
import time
import matplotlib.pyplot as plt

def quick_sort(arr, low, high):
    if low < high:
        pivot = partition(arr, low, high)
        quick_sort(arr, low, pivot - 1)
        quick_sort(arr, pivot + 1, high)

def partition(arr, low, high):
    p = arr[low]
    i = low + 1
    j = high

    while True:
        while i <= j and arr[i] <= p:
            i += 1
        while i <= j and arr[j] >= p:
            j -= 1
        if i <= j:
            arr[i], arr[j] = arr[j], arr[i]
        else:
            break

    arr[low], arr[j] = arr[j], arr[low]
    return j

arr = [5, 8, 1, 2, 6, 3, 9]
print("Before sorting:", arr)

quick_sort(arr, 0, len(arr) - 1)
print("After sorting:", arr)


sizes = [100, 500, 1000, 2000,4000,6000]
times = []

for size in sizes:
    arr = [random.randint(1, 10000) for _ in range(size)]
    
    start = time.time()
    quick_sort(arr, 0, len(arr) - 1)
    end = time.time()
    
    times.append(end - start)

plt.plot(sizes, times, marker='o')
plt.title("Quick Sort Time Complexity")
plt.xlabel("Input Size")
plt.ylabel("Execution Time (seconds)")
plt.grid(True)
plt.show()
