
def selectionsort(arr):
    for i in range(0,len(arr)):
        min=i

        for j in range(i+1,len(arr)):
            if arr[j]<arr[min]:
                min=j
        arr[i],arr[min]=arr[min],arr[i]
    return arr
arr=[]
n=int(input("enter number of element you want to enter:"))

for a in range(n):
    k=int(input("enter number of elements into an array"))
    arr.append(k)
print("the sorted elements are", selectionsort(arr))