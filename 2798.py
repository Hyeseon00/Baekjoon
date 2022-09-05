##2798-블랙잭##
import itertools

num=[]
all=[]
print_out=[0]

N, M=map(int,input().split())
num=map(int,input().split())
# 모든 경우의 수 저장
all=list(itertools.combinations(num,3))

for i in range(0,len(all)):
    result=0
    for j in range(0,3):
        result += all[i][j]
        
    # M보다 같거나 작은 수 중 가장 큰 수 구하기
    if result <= M:
        if len(print_out)==0:
            print_out[0]=result
        else:
            if result > print_out[0]:
                print_out[0]=result

print(print_out[0])