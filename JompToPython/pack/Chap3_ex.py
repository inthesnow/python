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


#6번


#7번


#8번


#9번


#10번


#11번


#12번
