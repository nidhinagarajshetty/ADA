import random
import time

def insert_sort(A):
    n=len(A)
    for i in range(1,n):
        v=A[i]
        j=i-1
        while j>=0 and A[j]>v:
            A[j+1]=A[j]
            j=j-1
        A[j+1]=v
n_list=[2000,1000,5000,4000,10000]
sort_time=[]
for n in n_list:
    arr=[random.randint(1,100) for _ in range(n)]
    s_t=time.time()
    insert_sort(arr)
    e_t=time.time()
    sort_time.append(e_t-s_t)
print(n)
print(sort_time)