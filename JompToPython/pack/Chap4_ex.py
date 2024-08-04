import sys
#1 개수 세기
N = int(input())
l = list(map(int, input().split()))
v = int(input())
sum=0
for i in range(len(l)):
    if v==l[i]:
        sum+=1
print(sum)

#2 X보다 작은 수
a, b = map(int, sys.stdin.readline().split())
l = list(map(int, sys.stdin.readline().split()))
sum = list()
for i in range(len(l)):
    if a != len(l): break
    if l[i]<b:
        sum.append(l[i])
print(*sum)

#3 최소, 최대
N = int(input())
l = list(map(int, sys.stdin.readline().split()))

x = l[0]
y = l[0]
for i in range(N):
    if N!=len(l): break
    if x > l[i]: x=l[i]
    if y < l[i]: y=l[i]
print(str(x)+" "+str(y))

#4 최댓값
import sys
lst = [0]
x=0
y=0
for i in range(1,10):
    N = int(sys.stdin.readline())
    lst.append(N)
    if x<=lst[i]: 
        x=lst[i]
        y=lst.index(x)
print(str(x))
print(str(y))

#5 공 넣기
import sys

N, M = map(int, input().split())
lst=[0]*N
for i in range(M):
    a, b, c = map(int, sys.stdin.readline().split())
    for j in range(a-1,b):
        lst[j] = c
print(*lst)

#6 공 바꾸기
import sys

N, M = map(int, input().split())
lst=list(range(1,N+1))
for i in range(M):
    a, b= map(int, sys.stdin.readline().split())
    tmp = lst[a-1]
    lst[a-1]= lst[b-1]
    lst[b-1]= tmp
print(*lst)

#7 과제 안 내신 분...?
import sys

t=list(range(1,31))
s=list(range(1,29))
a=0
for i in range(1, 29):
    s[i-1] = int(sys.stdin.readline())
    
for i in range(30):
    for j in range(28):
        if t[i]==s[j]:
            a=s[j]
            break
    if t[i]==a: continue
    else: print(str(t[i]))

#8 나머지
import sys

n=[0]*10
cnt=10
for i in range(10):
    n[i] = int(sys.stdin.readline())
    n[i] = n[i]%42
for i in range(10):
    for j in range(i+1,10):
        if n[i]==n[j]:
            cnt-=1
            break
print(cnt)

#9 바구니 뒤집기
import sys

n, m = map(int, sys.stdin.readline().split())
b = list(range(1,n+1))
for i in range(m):
    x, y = map(int, sys.stdin.readline().split())
    b[x-1:y]=reversed(b[x-1:y])
print(*b)

#10 평균
import sys

n = int(sys.stdin.readline())
x = list(map(int, sys.stdin.readline().split()))
tmp=0
sum=0
for i in range(n):
    if tmp <=x[i]: tmp=x[i]
for i in range(n):
    sum+=x[i]/tmp*100
print(sum/n)