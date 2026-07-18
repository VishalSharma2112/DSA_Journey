class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        n = len(nums)
        odd_even = [0]*n
        for i in range(n):
            if nums[i] % 2 != 0:
                odd_even[i] = 1
        
        freq_maps = {0: 1}
        count = 0
        prefix = 0
        for i in odd_even:
            prefix += i
            if prefix-k in freq_maps:
                count += freq_maps[prefix-k]
            freq_maps[prefix] = freq_maps.get(prefix, 0)+1
        return count