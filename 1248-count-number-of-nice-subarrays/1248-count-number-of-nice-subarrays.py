class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        n = len(nums)
        
        freq_maps = {0: 1}
        count = 0
        prefix = 0
        for index, i in enumerate(nums):
            prefix += nums[index]%2
            if prefix-k in freq_maps:
                count += freq_maps[prefix-k]
            freq_maps[prefix] = freq_maps.get(prefix, 0)+1
        return count