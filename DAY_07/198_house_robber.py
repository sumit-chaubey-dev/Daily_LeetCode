class Solution:
    def rob(self, nums: List[int]) -> int:
        st1 = 0
        st2 = 0
        for i in nums:
            current = max(st1+i, st2)
            st1 = st2
            st2 = current 
        return st2