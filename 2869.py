##2869-달팽이는 올라가고 싶다##
A=int(input())
B=int(input())
V=int(input())
day=0
nowHeight=0

while True:
    if V <= nowHeight:
        break
    else:
        day+=1
        nowHeight+=A
        if V > nowHeight:
            nowHeight-=B
            
print("----결과----")
print(day)