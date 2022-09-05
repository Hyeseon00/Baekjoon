##2231-분해합##
def hap(k):
    global answer
    while(k>0):
        answer+=(k%10)
        k//=10
    return answer

N=int(input())
result=0

for i in range(1, N):
    answer=0
    temp=hap(i)+i
    if temp==N:
        result=i
        print(i)
        break
    
#생성자가 없는 경우 0출력    
if result==0:
    print(0)