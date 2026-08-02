class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        ans = 0
        for i in range(32):
            bit_sum = 0
            for num in nums:
                if (num&1<<i) > 0:
                    bit_sum += 1
            if bit_sum%3:
                ans |= (1<<i)
        if ans & 1<<31: # it is negative
            return ans - 2**32
        return ans