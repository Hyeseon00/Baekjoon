##10870-피보나치 수 5##
def pibo(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return pibo(n-2) + pibo(n-1)

N=int(input())
print(pibo(N))