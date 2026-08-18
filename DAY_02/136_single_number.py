class Solution:
    def singleNumber(self, nums):
        seen = {}

        for num in nums:
            seen[num] = seen.get(num,0) + 1

        for k, v in seen.items():
            if v == 1:
                return k