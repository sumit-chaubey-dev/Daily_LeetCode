class Solution:
    def countSpecialIntegers(self, nums: list[int]) -> int:
        counti = 0
        seen = set()
        final = set()
        for i in range(1, len(nums)):
            if nums[i] != nums[i-1]:
                seen.add(nums[i-1])
            if nums[i] in seen:
                final.add(nums[i])
        seen.add(nums[-1])
        return len(set(nums) - final)