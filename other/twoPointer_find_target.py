arr=[1,2,3,5,6,9]
target=8

def checkTarger(arr):
    firstP=0
    secondP=len(arr)-1
    while firstP!=secondP:
        print("loop")
        if arr[firstP]+arr[secondP]==target:
            return [firstP,secondP]
        elif arr[firstP]+arr[secondP]>target:
            secondP-=1
        else:
            firstP+=1
    return False

value=checkTarger(arr)
print(f'{value}')