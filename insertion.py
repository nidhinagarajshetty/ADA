"""arr=list(map(int,input("enter the num:").split()))
n=len(arr)
for i in range(1,n):
    key =arr[i]
    j=i-1
    while j>=0 and arr[j]>key:
        arr[j+1]=arr[j]
        j-=1
    arr[j+1]=key
print("sorted aray",arr)"""

arr = []
n = int(input("enter number of elements"))

for i in range(n):
    arr.append(int(input("Enter number: ")))

arr.sort()
print("Sorted array:", arr)
