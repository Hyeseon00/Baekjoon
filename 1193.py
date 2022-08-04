##1193-분수찾기##
N = int(input())
A = 1
B = 1

##temp == 0 A증가 B감소, temp == 1 A감소 B증가## 
temp = -1

for i in range (1,N):
    if A==1 and B==1:
        B+=1
    elif A==1 and B!=1:
        if B%2!=0:
            B+=1
        else:
            temp=0
            A+=1
            B-=1
    elif A!=1 and B==1:
        if A%2!=0:
            temp=1
            A-=1
            B+=1
        else:
            A+=1
    else:
        if temp==0:
            A+=1
            B-=1
        else:
            A-=1
            B+=1

print("----결과----")
print("%d/%d"%(A, B))