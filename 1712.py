##1712-손익분기점##
A, B, C=map(int,input().split())
cnt=0

# A + B*x < C*x
if C!=B:
    cnt=A/(C-B)

if cnt>0:
    cnt += 1
    print(int(cnt))
else:
    print(-1)