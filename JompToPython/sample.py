import sys

n, m = map(int, sys.stdin.readline().split())
b = list(range(1,n+1))
for i in range(m):
    x, y = map(int, sys.stdin.readline().split())
    for x in y:
        print(i)