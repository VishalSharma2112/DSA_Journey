class Solution:
    def trailingZeroes(self, n: int) -> int:
        if n==0:
            return 0
        count = 0
        mul = 5
        while n//mul != 0:
            count += n//mul
            mul = mul*5
        return count