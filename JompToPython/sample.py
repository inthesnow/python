import sys

print(list(range(8)))
d=[[0]*3]*8
cnt=0
print(d)
for i in range(8):
    d[i][0]=cnt+1
    d[i][1]=cnt+2
    d[i][2]=cnt+3
    if i==5 or i==7: d[i].append()
    print("i = "+str(i)+", d["+str(i)+"] = "+str(d[i]))
    
    cnt+=3
    
#print(d)