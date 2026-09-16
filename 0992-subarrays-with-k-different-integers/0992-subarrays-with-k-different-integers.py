class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        def at_most(distinct):
            left = 0
            freq_maps = {}
            count = 0

            for right in range(len(nums)):
                freq_maps[nums[right]] = freq_maps.get(nums[right], 0)+1

                while len(freq_maps) > distinct:
                    freq_maps[nums[left]] -= 1

                    if freq_maps[nums[left]] == 0:
                        del freq_maps[nums[left]]

                    left += 1
                
                count += right-left+1
            return count
        return at_most(k) - at_most(k-1)