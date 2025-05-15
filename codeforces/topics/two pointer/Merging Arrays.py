arr1= [1, 2, 3, 4, 5]
arr2=[0,2,3,7,8]

def mergeArrays(arr1, arr2):
        firstP=0
        secondP=0
        arr3=[]
        while firstP<len(arr1) and secondP<len(arr2):
                print(f'firstP: {firstP} secondP: {secondP}')
                if arr1[firstP]<=arr2[secondP]:
                    arr3.append(arr1[firstP])
                    firstP+=1
                else:
                    arr3.append(arr2[secondP])
                    secondP+=1
        if firstP<=len(arr1):
            arr3.extend(arr1[firstP:])
        if secondP<=len(arr2):
            arr3.extend(arr2[secondP:])            

        return arr3

newarray=mergeArrays(arr1,arr2)
print(newarray)






