class Solution:
    def addDigits(self, num: int) -> int:
        r = str(num)
        while len(r) != 1:
            total = 0
            for d in r:
                total += int(d)
            r = str(total)
        return int(r)