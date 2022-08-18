##2869-달팽이는 올라가고 싶다##
A, B, V=map(int,input().split())
day=0
nowHeight=0

while (V-A)>nowHeight: #마지막 날에는 A만큼 올라가고 밤에 떨어지지 않음.
    day+=1
    nowHeight+=(A-B)

print(day+1)