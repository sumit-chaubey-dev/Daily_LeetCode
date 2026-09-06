class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
         n = len(nums)
         s_min = [0] * n
         current_min = float('inf')
         for i in range(n - 1, -1, -1):
            current_min = min(current_min, nums[i])
            s_min[i] = current_min
         p_max = -float('inf')
         for i in range(n):
            p_max = max(p_max, nums[i])
            if p_max - s_min[i] <= k:
                return i
         return -1