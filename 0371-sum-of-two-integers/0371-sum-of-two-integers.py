class Solution:
    def getSum(self, a: int, b: int) -> int:
        MASK = 0xFFFFFFFF
        MAX_INT = 0X7FFFFFFF

        while b!=0:
            XOR = a^b
            carry = (a&b)<<1

            a = XOR & MASK
            b = carry & MASK

        if a <= MAX_INT:
            return a
        else:
            return ~(a^MASK)