class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        left = 0
        max_len = -1
        freq_maps = {}

        for right in range(len(fruits)):
            freq_maps[fruits[right]] = freq_maps.get(fruits[right], 0)+1

            while len(freq_maps) > 2:
                freq_maps[fruits[left]] -= 1

                if freq_maps[fruits[left]] == 0:
                    del freq_maps[fruits[left]]

                left += 1
                
            max_len = max(max_len, right-left+1)
        return max_len