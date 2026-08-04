class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        if len(nums) == 2:
            return nums
        XOR = 0
        for i in nums:
            XOR ^= i
        bit_mask = XOR & -XOR
        XOR1 = 0
        XOR2 = 0
        for i in nums:
            if i & bit_mask == bit_mask:
                XOR1 ^= i
            else:
                XOR2 ^= i
        return [XOR1, XOR2]