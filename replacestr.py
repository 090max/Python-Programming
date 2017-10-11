#REPLACE FIRST CHARACTER OF YOUR STRING BY $
#Eg.
#adityajain
#output=adity$j$in
a=input("enter a string:")
x=list(a)
b=len(x)
y=x[0]
i=1
while i<=b-1 :
    if x[i]==y :
        x[i]='$'
    i=i+1
i=0
for i in range(b):
    print(x[i],end="")
