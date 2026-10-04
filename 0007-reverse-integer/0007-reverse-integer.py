class Solution:
    def reverse(self, x: int) -> int:
        sign = 0
        if x<0:
            sign = 1
            x = abs(x)
        ans = 0
        while x != 0:
            ans = ans*10 + (x%10)
            x //= 10
        if ans > 2**31 - 1:
            return 0

        if sign:
            return -ans
        else:
            return ans