##11653-소인수분해##
n=int(input())
list=[]

for i in range(2, n):
    for j in range(2, i):
        if(n%j==0):
            list.append(j)
            n/=j
            
list.sort()
for i in list:
    print(i)