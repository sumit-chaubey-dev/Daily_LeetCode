class Solution:
    def climbStairs(self, n: int) -> int:
        prev_1 = 1
        prev_2 = 2
        if n == 1:
            return 1
        for i in range(3, n+1):
            current = prev_1 + prev_2
            prev_1 = prev_2
            prev_2 = current
        
        return prev_2