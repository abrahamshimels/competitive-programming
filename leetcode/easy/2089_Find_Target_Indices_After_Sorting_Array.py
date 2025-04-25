# https://leetcode.com/problems/find-target-indices-after-sorting-array/description/
from typing import List
class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        newArr=[]
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[j]<nums[i]:
                    temp=nums[i]
                    nums[i]=nums[j]
                    nums[j]=temp
            if target==nums[i]:
                newArr.append(i)
        return newArr
    
nums = [1,2,5,2,3]
target = 5

n=Solution()
print(n.targetIndices(nums,target))
