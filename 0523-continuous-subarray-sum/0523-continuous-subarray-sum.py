class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        freq_maps = {0: -1}
        prefix = 0

        for i, num in enumerate(nums):
            prefix += num
            rem = prefix%k

            if rem in freq_maps:
                if i-freq_maps[rem] >= 2:
                    return True
            else:
                freq_maps[rem] = i
        return False