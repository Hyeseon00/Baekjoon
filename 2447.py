##2447-별 찍기-10##
def star(n, unit):
    reset=[] #제곱 수 만큼 커지는 새로운 리스트 생성
    if n==3:
        return unit
    else:
        for i in range(0,3):
            if i==1:
                for j in unit: #정사각형 중 가운데 비어있는 부분
                    reset.append(j+' '*len(unit)+j)
            else:
                for j in unit:
                    reset.append(j*3)
        return star(n//3, reset) #n=3까지 반복&리스트의 크기는 제곱씩 증가
            

N=int(input())
arr=["***", "* *", "***"] #가장 작은 단위
end = star(N, arr)

for i in end:
    print(i)