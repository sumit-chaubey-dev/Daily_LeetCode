class Solution:
    def sumDecoded(self, nums: list[int]) -> int:
        total = 0
        for num in nums:
            num = str(num)
            w = int(num[-1])
            x = int(num[:w])
            y = int(num[w:-1])

            total += pow(x, y, 10**9 + 7)

        return total % (10**9 + 7)