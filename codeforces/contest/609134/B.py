n=input()
arr=list(map(int,input().split()))

repeat={}
for i in arr:
    if i in repeat:
        repeat[i]+=1
    else:
        repeat[i]=1

maxHeight=max(repeat.values())
minTowers=len(repeat)
print(maxHeight,minTowers)