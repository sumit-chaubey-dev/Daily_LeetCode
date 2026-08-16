class Solution:
    def twoSum(self, nums, target):
        data = {}
        for i,num in enumerate(nums):
            ans = target - num
            if ans in data:
                return [data[ans], i]
            data[num] = i

