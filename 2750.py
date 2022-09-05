##2750-수 정렬하기##
N=int(input())

data=[]
for i in range(N):
    value=int(input())
    data.append(value)

for i in range(N):   #Bubble sort
    for j in range(N-1):
        if data[j]>data[j+1]: #오름차순 정렬
            temp=data[j]
            data[j]=data[j+1]
            data[j+1]=temp

#Insertion sort

for i in range(N):
    print(data[i])