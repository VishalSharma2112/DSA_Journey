class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        ans = []
        for i in range(len(nums)):
            if i>0 and nums[i] == nums[i-1]:
                continue
            fixed = nums[i]
            start = i+1
            end = len(nums)-1
            while(start < end):
                if nums[start] + nums[end] > -fixed:
                    end -= 1
                elif nums[start] + nums[end] < -fixed:
                    start += 1
                else:
                    ans.append((nums[i], nums[end], nums[start]))
                    end -= 1
                    start += 1

                    while start < end and nums[start] == nums[start-1]:
                        start += 1
                    while start < end and nums[end] == nums[end+1]:
                        end -= 1
        return ans  