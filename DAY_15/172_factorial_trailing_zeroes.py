class Solution:
    def trailingZeroes(self, n: int) -> int:
        count = 0 
        while n > 0:
            r = n//5
            count += r
            n = n//5
        return count