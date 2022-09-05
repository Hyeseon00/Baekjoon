##2751-수 정렬하기2##
#Merge sort
def mergeSort(list,p,q): #q= inclusive
	if p>= q: return #재귀 종료 조건
	mid = (p + q) // 2
	mergeSort(list, p, mid) #재귀
	mergeSort(list, mid+ 1, q) #재귀
	merge(list, p, mid + 1, q)

def merge(list, left, right, end):
	merged = [] #정렬된 data 값 저장 리스트
	l, r = left, right
	while l < right and r <= end:
		if list[l] <= list[r]:
			merged.append(list[l])
			l +=1 #다음 비교 리스트(왼) 순서 +1
		else:
			merged.append(list[r])
			r +=1 #다음 비교 리스트(오) 순서 +1 : r번째 리스트가 정렬 data 리스트에 추가되었으므로,
	while l < right:
		merged.append(list[l])
		l +=1
	while r <= end:
		merged.append(list[r])
		r+=1

	l = left
	for n in merged: #정렬된 data 리스트(merged)를 원래 배열에 저장
		list[l] = n
		l +=1


N=int(input())

data=[]
for i in range(N):
    value=int(input())
    data.append(value)

sorted = mergeSort(data, 0, len(data) - 1)
for i in range(N):
    print(data[i])