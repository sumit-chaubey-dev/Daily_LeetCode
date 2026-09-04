class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        for i in range(len(nums)):
            inst = max(nums[:i+1]) - min(nums[i:])
            if inst <= k:
                return i
        else:
            return -1