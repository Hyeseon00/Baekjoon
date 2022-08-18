##2775-부녀회장이 될테야##

##거주자 수 counting function- v1:층수 v2:호수##
def resident(v1, v2):
    resNum = 0
    temp = []
    apt = []
    for i in range(0,v1+1):
        if(i==0):
            for t in range(0,v2):
                temp.append(t+1)
        else:
            for t in range(0,v2):
                if (t==0):
                    resNum = 1
                    temp.append(resNum)
                else:
                    resNum = 0
                    for r in range(0,t+1):
                        resNum += apt[i-1][r]
                    temp.append(resNum) 
        apt.append(temp)
        temp = []
    return apt[v1][v2-1]
 
T=int(input())

for i in range(0,T):
    k, n =map(int,input().split())
    result = resident(k, n)
    print(result)