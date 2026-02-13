import random
import time
import matplotlib.pyplot as plt
def quick_sort(arr, low, high): 
    if low < high:
        pivot = partition(arr, low, high)
        quick_sort(arr, low, pivot - 1)
        quick_sort(arr, pivot + 1, high)

def partition(arr, low, high):
    pivot = arr[high]     
    i = low - 1           
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1
arr = [5, 8, 1, 2, 6, 3, 9]
print("Before sorting:", arr)
quick_sort(arr, 0, len(arr) - 1)
print("After sorting:", arr)
sizes = [100, 500, 1000, 2000 ,4000, 5000]
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
plt.ylabel("Time (seconds)")
plt.grid(True)
plt.show()