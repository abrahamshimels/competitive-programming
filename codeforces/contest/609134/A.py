n=int(input())
arr=list(map(int,input().split()))

if 0 in arr:
    print(0)

else:
    print(min(abs(i) for i in arr))
    


