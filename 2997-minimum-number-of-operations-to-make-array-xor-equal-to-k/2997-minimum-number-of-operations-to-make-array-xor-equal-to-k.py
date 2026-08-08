class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        xor = 0
        count = 0
        for i in nums:
            xor ^= i
        if xor == k:
            return 0
        for i in range(32):
            if(xor&1 != k&1):
                count += 1
            xor >>= 1
            k >>= 1
        return count