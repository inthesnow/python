import sys
#1번
a = int(input())
for i in range(1,10): print(str(a) + " * " + str(i) + " = " + str(a*i))

#2번
T = int(input())
x=[]
for i in range(T):
    a, b=map(int, input().split())
    x.append(a+b)
for i in range(T):
    print(x[i])

#3번
n = int(input())
x = 0
for i in range(1,n+1): x+=i
print(x)

#4번
X = int(input())
N = int(input())
s = 0
for i in range(N): 
    a, b=map(int, input().split())
    s+= a*b
if X==s: print("Yes")
else: print("No")

#5번
N = int(input())//4
l = ""

for i in range(N):
    l+="long "

print(l+"int")

#6번
T=int(input())
for i in range(T):
    a, b = map(int, sys.stdin.readline().split())
    print (a+b)

#7번
T=int(input())
for i in range(T):
    a, b = map(int, sys.stdin.readline().split())
    print (a+b)

#8번
T=int(input())
for i in range(T):
    a, b = map(int, sys.stdin.readline().split())
    print ("Case #"+str(i+1)+": "+str(a)+" + " +str(b) + " = "+str(a+b))

#9번
N = int(input())
s = ""
for i in range(N):
    s+="*"
    print(s)

#10번
N = int(input())

for i in range(1,N+1):
    a=" "*(N-i)
    a+="*"*i
    print(a)

#11번
while True:
    a, b= map(int, sys.stdin.readline().split())
    if a==0 and b==0:
        break
    print(a+b)

#12번
while True:
    try:
        a, b= map(int, sys.stdin.readline().split())
        print(a+b)
    except:
        break
