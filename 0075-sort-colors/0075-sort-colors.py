class Solution:
    def sortColors(self, nums: List[int]) -> None:
        i = 0
        j = len(nums) - 1

        while j > i:
            if nums[j] == 2:
                j -= 1
                continue
            if nums[i] == 2:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
                j -= 1
            else:
                i += 1
        if nums[j] == 2:
            j -= 1
            
        a = 0
        b = j
        while b > a:
            if nums[b] == 1:
                b -= 1
                continue
            if nums[a] == 1:
                nums[a], nums[b] = nums[b], nums[a]
                a += 1
                b -= 1
            else:
                a += 1        