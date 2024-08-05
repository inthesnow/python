#1 문자와 문자열
s = input()
print(s[int(input())-1])

#2 단어 길이 재기
print(len(input()))

#3 문자열
n = int(input())
for i in range(n) :
    s=input()
    print(str(s[0]+str(s[-1])))

#4 아스키 코드
print(ord(input()))

#5 숫자의 합
n = int(input())
s = input()
sum = 0
for i in range(n):
    sum +=int(s[i])
print(str(sum))

#6 알파벳 찾기
s = input()
sum = [-1]*26
for i in reversed(range(len(s))):
    for j in range(26):
        if sum[j]==i: break
        if ord(s[i])==j+97: sum[j]=i
print(*sum)

#7 문자열 반복
import sys
t=int(input())
s=""
for i in range(t):
    n, x = map(str, sys.stdin.readline().split())
    for j in range(len(x)):
        a=x[j]*int(n)
        s+=a
    print(s)
    s=""

#8 단어의 개수
import sys

s = sys.stdin.readline().split()
print(len(s))

#9 상수
import sys

x, y= map(str, sys.stdin.readline().split())
x=int(x[2])*100+int(x[1])*10+int(x[0])
y=int(y[2])*100+int(y[1])*10+int(y[0])
if x>=y: print(x)
else: print(y)

#10 다이얼
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