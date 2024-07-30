import sys

N, M = map(int, input().split())
a, b, c = 0
for i in range(M):
    lst=list(map(int, sys.stdin.readline().split()))
    a = lst[0]
    b = lst[1]
    c = lst[2]
    