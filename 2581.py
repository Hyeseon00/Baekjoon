##2581-소수#
m,n=map(int,input().split())
value=0
list=[]

for i in range(m,n+1):
    error=0
    if i>1:
        for j in range(2,i):
            if(i%j==0): #소수가 아니다.
                error=-1
                break
        if error==0:
            list.append(i)

for i in range(0,len(list)):
    value += list[i]
    
if value==0:
    print(-1)
else:
    print(value)
    print(list[0])