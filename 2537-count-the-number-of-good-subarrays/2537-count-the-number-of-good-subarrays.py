class Solution:
    def countGood(self, nums: List[int], k: int) -> int:
        n = len(nums)
        count = 0
        left = 0
        maps = {}
        pair = 0

        for right in range(n):
            pair += maps.get(nums[right], 0)
            maps[nums[right]] = maps.get(nums[right], 0)+1
            
            while pair >= k:
                count += n-right
               
                maps[nums[left]] -= 1

                pair -= maps[nums[left]]
                
                if maps[nums[left]] == 0:
                    del maps[nums[left]]
                
                left += 1
        return count

