class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        freq_maps = {0: 1}
        prefix = 0
        count = 0
        for i in nums:
            prefix += i
            rem = prefix%k

            if rem in freq_maps:
                count += freq_maps[rem]
            freq_maps[rem] = freq_maps.get(rem, 0)+1
        return count