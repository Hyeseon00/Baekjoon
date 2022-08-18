##9020-골드바흐의 추측##
T = int(input())
testcase=list(map(int,input().split()))
q=0

#2보다 큰 수 n - 소수의 합으로 구성됨. (n-k=t 일때, k와 t가 모두 소수)
for i in testcase:
    cnt=0
    arr=[0,0,0]
    print(i, "의 골드바흐 파티션")
    for j in range(3,i,2):
        t = i-j
        if j<=t:
            for k in range(3,t,2):
                for p in range(2,k):
                    if k%p==0:
                        q+=1
                if q==0:
                    if j//k<2 and t%k!=0:
                        if arr[0]==0:
                            arr[0]=t-j
                            temp1=j
                            temp2=t
                        else:
                            if arr[0]>t-j: #두 소수의 차이가 가장 작은 경우 새로 저장
                                arr[0]=t-j
                                arr[1]=j
                                arr[2]=t
                                cnt=1
    if cnt==1:
        print(arr[1], arr[2])
    else:
        print(temp1, temp2)
    