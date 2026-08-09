class Solution:
    def reverse(self, x: int) -> int:
        if x<0:
            word = str(abs(x))
            number = -int(word[::-1])
            if -2**31 <= number <= (2**31) - 1:
                return number
            else:
                return 0
        else:
            word = str(abs(x))
            number = int(word[::-1])
            if -2**31 <= number <= (2**31) - 1:
                return number
            else:
                return 0