n=int(input("enter a number"))
x=0
y=1
if(x<n):
    for z in range(0,n):
        z=x+y
        print(x)
        x=y
        y=z
