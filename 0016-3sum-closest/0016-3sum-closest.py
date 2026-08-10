class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        closest_sum = 0
        MIN = float('inf')
        n = len(nums)
        for i in range(n):
            start = i+1
            end = n-1
            while start<end:
                current_sum = nums[i]+nums[start]+nums[end]
                diff = abs(current_sum-target)
                if diff < MIN:
                    MIN = diff
                    closest_sum = current_sum
                if current_sum < target:
                    start += 1
                elif current_sum > target:
                    end -= 1
                else:
                    return current_sum
        return closest_sum