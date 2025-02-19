def add (*n):
    print(n)
    print(type(n))
    sum=0
    for i in n:
        sum=sum+1
    return sum
n=add(2,4,5,6)
print(n)