##10250-ACM호텔##
T=int(input())
arr1 = []
arr2 = []
roomNum=0

for i in range(0,T):
    for k in range(0,3):
        value = int(input())
        arr1.append(value)
    arr2.append(arr1)
    arr1=[]

print("----결과----")      
for i in range(0,T):
    H=arr2[i][0]
    W=arr2[i][1]
    N=arr2[i][2]
    if (N//H)+1 < 10:
        roomNum = str(N%H)+str(0)+str((N//H)+1)
    else:
        roomNum = str(N%H)+str((N//H)+1)
    print(roomNum)