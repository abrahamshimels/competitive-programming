#User function Template for python3

class Solution:
    def arraySortedOrNot(self, arr) -> bool:
        arrLength=len(arr)
        baseNum=arr[0]
        for i in range(1, arrLength):
            if arr[i] < arr[i - 1]:
                return False
        return True