T = input()
list = []
for i in range(int(T)) : 
    c = input().split(' ')
    list.append(int(c[0])+int(c[1]))

for j in range(int(T)) : 
    print(list[j])