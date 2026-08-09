class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        ans = set()
        for i in range(len(nums)):
            fixed = nums[i]
            start = i+1
            end = len(nums)-1
            while(end > start):
                if nums[start] + nums[end] > abs(fixed):
                    end -= 1
                elif nums[start] + nums[end] < abs(fixed):
                    start += 1
                else:
                    ans.add((nums[i], nums[end], nums[start]))
                    end -= 1
                    start += 1
        return list(ans)   