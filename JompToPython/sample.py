import sys

n, m = map(int, sys.stdin.readline().split())
b = list(range(1,n+1))
for i in range(m):
    x, y = map(int, sys.stdin.readline().split())
    tl=list(range(x,y))
    print(tl)
    for j in range(x,y):
        tmp=tl[j-1]
        tl[j-1]=tl[y-j]
        tl[y-j]=tmp
    print(tl)