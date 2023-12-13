class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        map = {}
        n = len(nums)
        #Create Map
        for i in nums:
            map[i] = target - i
        
        for i in range(n):
            complement = target - nums[i]
            if complement in map:
                if i == nums.index(complement):
                    pass
                else:
                    return [i, nums.index(complement)]
        


test =  Solution()
print(test.twoSum([3,3],6))

import turtle
turtle.f