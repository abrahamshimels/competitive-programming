# https://www.geeksforgeeks.org/problems/selection-sort/1
#User function Template for python3

class Solution: 
    def selectionSort(self, arr):
        #code here
        for i in range(len(arr)):
            min_idx=i
            for j in range(i+1,len(arr)):
                if arr[j]<arr[min_idx]:
                    min_idx=j
            arr[min_idx], arr[i]=arr[i],arr[min_idx]
            
        return arr

arr= [4, 1, 3, 9, 7]      
n=Solution()
print(n.selectionSort(arr))