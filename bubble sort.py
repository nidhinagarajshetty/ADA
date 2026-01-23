
n=int(input("Enter the elements:"))
arr=list(map(int,input("enter elements:").split()))
for i in range(n- 1):
    for j in range (n-i-1):
        if arr[j]>arr[j+1]:
            arr[j],arr[j+1]=arr[j+1],arr[j]
print("Sorted list:", arr)