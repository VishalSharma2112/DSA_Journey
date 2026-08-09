class Solution:
    def reverse(self, x: int) -> int:
        sign = -1 if x < 0 else 1

        number = int(str(abs(x))[::-1]) * sign

        if -2**31 <= number <= 2**31 - 1:
            return number

        return 0