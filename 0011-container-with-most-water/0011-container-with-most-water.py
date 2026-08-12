class Solution:
    def maxArea(self, height: List[int]) -> int:
        n = len(height)
        i = 0
        j = n-1
        area = 0
        while j > i:
            h = min(height[i], height[j])
            width = j-i
            area = max(area, h*width)

            if height[j] > height[i]:
                i += 1
            else:
                j -= 1
        return area