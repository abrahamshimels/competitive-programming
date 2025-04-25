from typing import List

class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        newArr=[]
        for num in nums:
            count=0
            for val in nums:
                if val < num:
                    count=count+1
            newArr.append(count)
        return newArr
        
nums = [7,7,7,7]

n = Solution()
print(n.smallerNumbersThanCurrent(nums))