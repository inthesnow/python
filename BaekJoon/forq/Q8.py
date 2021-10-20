import sys

T = int(sys.stdin.readline())
x = []
y = []
r = []

for i in range(T):
    a,b = map(int, sys.stdin.readline().split())
    x.append(a)
    y.append(b)
    r.append(a+b)

for i in range(T):
    print("Case #" + str(i+1) + ": " + str(x[i]) + " + "+ str(y[i]) + " = " + str(r[i]))