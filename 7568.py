##7568-덩치##
N=int(input())
arr=[]
rank=[]
# 사람별 (몸무게,키) 저장
for i in range(N):
    x, y=map(int,input().split())
    arr.append((x,y))

#자신보다 큰 덩치를 가진 이가 k명이면 나의 등수는 k+1
for i in range(N):
    cnt = 0
    for j in range(N):
        #몸무게 및 키 모두 큰 경우만 count
        if arr[i][0] < arr[j][0] and arr[i][1] < arr[j][1]:
            cnt += 1
    rank.append(cnt + 1)

for i in range(N):
    print(rank[i], end=" ")