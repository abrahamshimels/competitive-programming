# https://leetcode.com/problems/find-three-consecutive-integers-that-sum-to-a-given-number/
class Solution(object):
    def sumOfThree(self, num):
        middle=num//3
        if num % 3 == 0:
            return [middle-1,middle,middle+1]
        else:
            return []


num = 4
solution=Solution()
print(solution.sumOfThree(num))