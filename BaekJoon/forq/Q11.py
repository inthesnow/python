import sys

n = sys.stdin.readline().split()
n = list(map(int, n))
a = sys.stdin.readline().split()
a = list(map(int, a))

x=""

for i in range(n[0]) :
    if a[i] < n[1] :
        x +=str(a[i])+" "

print(x.rstrip())