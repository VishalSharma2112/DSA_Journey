class Solution:
    def trap(self, height: List[int]) -> int:
        left_max = 0
        right_max = 0
        total = 0
        i = 0
        j = len(height)-1
        while i < j:
            if height[i] < height[j]:
                if height[i] < left_max:
                    total += left_max-height[i]
                else:
                    left_max = height[i]
                i += 1
            else:
                if height[j] < right_max:
                    total += right_max - height[j]
                else:
                    right_max = height[j]
                j -= 1
        return total