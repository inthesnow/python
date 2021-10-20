import sys

n = int(sys.stdin.readline())

for i in range(1, n+1) :
    r=" "*(n-i)
    r+="*"*i
    print(r)