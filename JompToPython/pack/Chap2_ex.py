#1번
a, b= map(int, input().split())
if(a>b) : print(">")
elif(a<b) : print("<")
else : print("==")

#2번
a = int(input())
if(a>=90) : print("A")
elif(a>=80) : print("B")
elif(a>=70) : print("C")
elif(a>=60) : print("D")
else : print("F")

#3번
a = int(input())
if a%400==0 : print("1")
elif a%100==0 : print("0")
elif a%4==0 : print("1")
else : print("0")

#4번
a=int(input())
b=int(input())
if a>0 : 
    if b>0 : print("1")
    else : print("4")
else :
    if b>0 : print("2")
    else : print("3")

#5번
a, b= map(int, input().split())
if b-45<0: 
    if a==0: print(str(23) + " " + str(60+(b-45)))
    else: print(str(a-1) + " " + str(60+(b-45)))
else: 
    print(str(a) + " " + str(b-45))

#6번
a, b= map(int, input().split())
c=int(input())
d=c//60
e=c%60
if b+e>59: 
    if a+d+1>23: print(str(a+d-23)+" "+ str(b+e-60))
    else: print(str(a+d+1)+" "+ str(b+e-60))
else:
    if a+d>23: print(str(a+d-24)+" "+ str(b+e))
    else: print(str(a+d)+" "+ str(b+e))

#7번
a, b, c = sorted(map(int, input().split()))
if a==b:
    if b==c: print(a*1000+10000)
    else: print(a*100+1000)
elif a>b:
    if a==c: print(a*100+1000)
    else:
        if b==c: print(b*100+1000)
        elif a>c: print(a*100)
        else: print(c*100)
else:
    if a==c: print(a*100+1000)
    else:
        if b==c: print(b*100+1000)
        elif b>c: print(b*100)
        else: print(c*100)
        