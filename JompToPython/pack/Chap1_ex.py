#1번
print("Hello World!")

#2번
a, b = map(int, input().split())
print(a+b)

#3번
a, b = map(int, input().split())
print(a-b)

#4번
a, b = map(int, input().split())
print(a*b)

#5번
a, b = map(int, input().split())
print(a/b)

#6번
a, b = map(int, input().split())
print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a%b)

#7번
a = input()
print(a+"??!")

#8번
a = int(input())
print(a-543)

#9번
a, b, c = map(int, input().split())
print((a+b)%c)
print(((a%c)+(b%c))%c)
print((a*b)%c)
print((a%c)*(b%c)%c)

#10번
a = int(input())
b = int(input())
print(a*(b%10))
print((a*((b%100)-(b%10)))//10)
print(a*(b//100))
print(a*b)

#11번
a, b, c = map(int, input().split())
print(a+b+c)

#12번
print("\\    /\\")
print(" )  (  ')")
print("(  /  )")
print(" \\(__)|")

#13번
a='''|\\_/|
|q p|   /}
( 0 )\"\"\"\\
|\"^\"`    |
||_/=\\\\__|'''
print(a)