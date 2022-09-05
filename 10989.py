##10989-수 정렬하기3##
N=int(input())

data=[]
for i in range(N):
    value=int(input())
    data.append(value)
    
#Counting sort
count = [0] * (max(data) + 1) #각 원소의 개수 counting/원소의 최대값까지 인덱스로 사용
for i in data: #숫자 i가 배열에 몇개 존재하는지 저장
    count[i] += 1
    
for i in range(1, len(count)):#누적합 계산/data에 담긴 원소를 정렬하기 위함
    count[i] += count[i-1]

result = [0] * (len(data)) #정렬된 data 리스트
for i in data: #data의 원소를 정렬된 위치에 삽입
    idx = count[i]
    result[idx - 1] = i
    count[i] -= 1

print("----------결과 출력----------")
for i in range(N):
    print(result[i])