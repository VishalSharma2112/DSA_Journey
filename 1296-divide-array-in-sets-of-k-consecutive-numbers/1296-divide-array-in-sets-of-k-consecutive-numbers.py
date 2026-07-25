class Solution:
    def isPossibleDivide(self, nums: List[int], k: int) -> bool:
        if len(nums) % k != 0:
            return False

        freq_maps = {}
        sorted_nums = sorted(nums)
        for i in sorted_nums:
            freq_maps[i] = freq_maps.get(i, 0)+1
        
        for card in sorted_nums:
            if freq_maps[card] == 0:
                continue
            
            for nxt in range(card, card+k):
                if freq_maps.get(nxt, 0) == 0:
                    return False
                freq_maps[nxt] -= 1
        return True