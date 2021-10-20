import sys

T = int(input()) #Test case
r = []
for i in range(T):
    a,b = map(int, sys.stdin.readline().split())
    r.append(a+b)
for i in range(T):
    print(r[i])