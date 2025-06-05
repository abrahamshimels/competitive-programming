def maximumproduct(digits):
    best=0
    for i in range(len(digits)):
        newDigits=digits.copy()
        newDigits[i]+=1

        product=1
        for num in newDigits:
            product *=num
        if product>best:
            best = product

        return best

t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    print(maximumproduct(arr))