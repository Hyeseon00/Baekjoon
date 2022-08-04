##2839-설탕배달##
N=int(input())
num=0

while N>0:
    if N<3:
        break
    elif (N%5)%3 == 0:
        num+=N//5
        N%=5
        num+=N//3
        N%=3
    else:
        if N%5==0:
            num+=N//5
            N%=5
        elif N%3==0:
            num+=N//3
            N%=3
        else:
            break
        
print("----결과----")
if N!=0:
    print(-1)
else:
    print(num)