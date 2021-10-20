import sys

T = int(sys.stdin.readline()) #Test case
r = []

for i in range(T):
    a,b = map(int, sys.stdin.readline().split())
    r.append(a+b)

for i in range(T):
    print("Case #" + str(i+1) + ": " + str(r[i]))