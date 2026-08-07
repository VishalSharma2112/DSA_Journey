class Solution:
    def getMaximumXor(self, nums: List[int], maximumBit: int) -> List[int]:
        max_bit = (2**maximumBit)-1
        ans = []
        pxor = [0]
        for i in nums:
            pxor.append(pxor[-1]^i)
        for i in range(len(nums), 0, -1):
            ans.append(pxor[i]^max_bit)            
        return ans