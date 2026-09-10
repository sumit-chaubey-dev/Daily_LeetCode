class Solution:
    def countCommas(self, n: int) -> int:
         total_commas = 0
         k = 1
         while True:
            lower_bound = 10 ** (3 * k)
            if lower_bound <= n:
                total_commas += (n - lower_bound + 1)
                k += 1
            else:
                break
         return total_commas
