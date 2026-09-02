class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        left = 0
        W_count = 0
        min_W = float('inf')
        for right in range(len(blocks)):
            if blocks[right] == 'W':
                W_count += 1
            
            if right-left+1 == k:
                min_W = min(min_W, W_count)
                if blocks[left] == 'W':
                    W_count -= 1
                left += 1
        return min_W