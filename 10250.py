##10250-ACM호텔##
T=int(input())
roomNum=0

for i in range(0,T):
    H, W, N =map(int,input().split())
    if (N%H != 0):
        roomNum = (N%H)*100+((N//H)+1)
    else:
        roomNum = H*100+(N//H)
    print(roomNum)