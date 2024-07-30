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
