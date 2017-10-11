#DECIMAL TO BINARY
#Eg.
#123
#output=1101111
a=int(input("enter a no."))
b=[]
c=0
while(a>0):
    b.append(a%2)
    a=a//2
for i in b:
    print(i,end="")
