yr=int(input("enter the year"))
m=int(input("enter the month"))
d=int(input("enter the day"))
if(d<28 and m==2):
    print(yr,"-",m,"-",d+1)
if(d==28 and m==2 and yr%4!=0):
    print(yr,"-",3,"-",1)
if(d==28 and m==2 and yr%4==0):
    print(yr,"-",2,"-",29)
if(d==29 and m==2):
    print(yr,"-",3,"-",1)
    
elif(d<30 and m<13):
    print(yr,"-",m,"-",d+1)
elif(d==30 and (m==4 or m==6 or m==9 or m==11)):
    print(yr,"-",m+1,"-",1)
elif(d==31 and m==12):
    print(yr+1,"-",1,"-",1)
elif(d==30):
    print(yr,"-",m,"-",d+1)
elif(d==31 and m<=12):
     print(yr,"-",m+1,"-",1)
else:
    print("wrong date is entered")
