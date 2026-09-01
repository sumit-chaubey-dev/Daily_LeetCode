class Solution:
    def reverse(self, x: int) -> int:
        rev = 0
        is_negative = False
        if x < 0:
            is_negative = True
            x = x * -1
            
        while x > 0:
            digit = x % 10
            rev = (rev * 10) + digit
            x = x // 10

        if is_negative:
            rev = rev * -1
        if rev < -2**31 or rev > 2**31 - 1:
            return 0

        return rev
