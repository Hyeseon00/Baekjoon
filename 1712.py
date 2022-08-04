##1712-손익분기점##
A = int(input())
B = int(input())
C = int(input())

totalCost = A
totalIncome = 0
salesVloume = 0

while (totalIncome - totalCost) <= 0 :
    if B>C:
        break
    salesVloume += 1
    totalCost += B
    totalIncome += C

print("----결과----")
if B>C:
    print(-1)
else :
    print(salesVloume)