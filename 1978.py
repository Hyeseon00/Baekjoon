##1978-소수 찾기#
N=int(input())
num=list(map(int,input().split()))
cnt=0

for i in num:
    error=0
    if i>1:   
        for j in range(2,i):
            if(i%j==0): #소수가 아니다.
                error=-1
                break
        if error==0:
            cnt+=1
print(cnt)