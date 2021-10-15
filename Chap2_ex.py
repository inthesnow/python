#1번
avg = (80+75+55)/3
print("1번. 홍길동 씨의 평균 점수는 %6s" % avg)

#2번
a = 13
if(a%2==1) : print("홀수")
else  : print("짝수")

#3번
ymd = '881120-1068234'
print(ymd.split('-'))

#4번
pin = "881120-1068234"
print("성별을 나타내는 숫자 : "+pin[7])

#5번
a = "a:b:c:d"
print(a.replace(':','#'))

#6번
list = [1, 3, 5, 4, 2]
list.sort(reverse=True)
print(list)

#7번
lits = ['Life', 'is', 'too', 'short'] 
print(' '.join(lits))

#8번
tuple1 = (1,2,3)
tuple2 = (4,)
print (tuple1+tuple2)

#9번
#3. key에는 list같은 변경이 가능한 값이 들어갈 수 없다.

#10번
a = {'A':90, 'B':80, 'C':70}
print (a['B'])

#11번
a = [1, 1, 1, 2, 2, 3, 3, 3, 4, 4, 5]
print (set(a))

#12번
a = b = [1, 2, 3]
a[1] = 4
print(b)
#바뀐다. > a에 넣은 list는 [1,2,3]이 아닌 b이다.
#즉, [1,2,3]에 2>4로 바꾼것이 아닌 b[1] = 4로 바꾼 것과 같다.