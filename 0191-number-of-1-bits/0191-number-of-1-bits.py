class Solution:
    def hammingWeight(self, n: int) -> int:
        bits = n.bit_length()
        count = 0
        for i in range(0, bits):
            if n & 1<<i:
                count += 1
        return count