n=int(input("Enter ypur number:  "))
x=y=n
digit=0
while n>0:
    digit=digit+1
    n=n//10
sum=0
while y>0:
    last_digit=y%10
    sum=sum+last_digit**digit
    y=y//10

    if n==sum:
        print(f'{x} is armstrong')

    else:
        print(f'{y} is armstrong')   