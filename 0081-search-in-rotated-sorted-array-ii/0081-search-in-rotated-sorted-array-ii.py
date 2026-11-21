class Solution:
    def search(self, nums: list[int], target: int) -> bool:
        low = 0
        high = len(nums)-1
        while high>low:
            mid = low+(high-low)//2

            if nums[mid]==target:
                return True
            print(nums[low], nums[mid], nums[high])
            if nums[low] == nums[mid] == nums[high]:
                low += 1
                high -= 1
            elif nums[low] <= nums[mid]:
                if target <= nums[mid] and nums[low] <= target:
                    high = mid-1
                else:
                    low = mid+1
            else:
                if target >= nums[mid] and target <= nums[high]:
                    low = mid+1
                else:
                    high = mid-1
        return target == nums[high]
            