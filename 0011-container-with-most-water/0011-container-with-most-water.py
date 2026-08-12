class Solution:
    def maxArea(self, height: List[int]) -> int:
        n = len(height)
        i = 0
        j = n-1
        MAX = 0
        while i < j:
            h = min(height[i], height[j])
            width = j-i
            MAX = max(MAX, h*width)

            if height[i] < height[j]:
                i += 1
            else:
                j -= 1
        return MAX