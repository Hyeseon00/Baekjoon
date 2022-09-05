##25305-커트라인##
N, k=map(int, input().split())

score=map(int,input().split())
score=list(score)

for i in range(N): #Bubble sort
    for j in range(N-1):
        if score[j]<score[j+1]: #내림차순 정렬
            temp=score[j]
            score[j]=score[j+1]
            score[j+1]=temp

print(score[k-1])