n=int(input("enter a number n:"))
a=n/2
while a*a>n:
    a=a-0.0000001
print(a)