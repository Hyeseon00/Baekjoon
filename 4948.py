##4948-베르트랑 공준##
list=[]

while True: #Each test case number saving
    n=int(input())
    if (n!=0):
        list.append(n)
    else:
        break

for i in range(0,len(list)):
    k=list[i]
    cnt=0
    for j in range(k+1,2*k+1):
        error=0
        for t in range(2,j):
            if (j%t==0):
                error+=1
        if error==0:
            cnt+=1
    print(cnt)