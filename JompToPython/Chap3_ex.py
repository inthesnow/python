#Q1.
print ("shirt")

#Q2.
sum=0
i=1
while i<=1000 :
    if i%3==0 :
        sum += i
    i+=1
print (sum)


#Q3.
str = "*"
i=1
while i<6 :
    print(str*i)
    i+=1

#Q4.
for i in range(1,101) :
    print(i)

#Q5.
A = [70, 60, 55, 75, 95, 90, 80, 80, 85, 100]
sum = 0
avg = 0
for i in A :
    sum+=int(i)
avg = sum/len(A)
print (avg)

#Q6.
numbers = [1, 2, 3, 4, 5]
result = [number * 2 for number in numbers if number%2==1]
print (result)