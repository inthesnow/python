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
    