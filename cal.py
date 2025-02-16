while True:
    print("1.Add\n 2.Sub\n 3.Multi\n 4.Div\n 5.Off")

    n=int(input("Enter your choice :"))
    if n==1:
        x=int("enter your 1st value")
        y=int("enter your 2nd value")
        z=x+y
        print(f'Add of {x} and {y} is {z}')
    
    if n==2:
        x=int("enter your 1st value")
        y=int("enter your 2nd value")
        z=x-y
        print(f'Sub of {x} and {y} is {z}')
    
    if n==3:
        x=int("enter your 1st value")
        y=int("enter your 2nd value")
        z=x*y
        print(f'Multi of {x} and {y} is {z}')

    if n==4:
        x=int("enter your 1st value")
        y=int("enter your 2nd value")
        z=x/y
        print(f'Div of {x} and {y} is {z}')
    
    