##1929-소수 구하기##
m,n=map(int,input().split())

for i in range(m,n+1):
    error=0
    if i>1:
        for j in range(2,i):
            if (i%j==0):
                error+=1
        if error==0:
            print(i)