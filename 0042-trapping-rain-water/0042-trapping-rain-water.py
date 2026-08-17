class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        suffix_max = height.copy()
        for i in range(n-2, -1, -1):
            suffix_max[i] = max(suffix_max[i+1], height[i])

        prefix_max = 0
        total = 0 
        for i in range(n):
            prefix_max = max(prefix_max, height[i])
            if height[i]<=prefix_max and height[i]<=suffix_max[i]:
                total += min(prefix_max, suffix_max[i])-height[i]
        return total