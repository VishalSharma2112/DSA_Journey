class Solution:
    def minWindow(self, s: str, t: str) -> str:
        t_map = {}
        s_map = {}

        def check(s_map, t_map):
            for i in t_map:
                if i not in s_map:
                    return False
                if t_map[i] > s_map[i]:
                    return False
            return True


        for i in t:
            t_map[i] = t_map.get(i, 0)+1

        left = 0
        min_len = float('inf')
        ans = ""

        for right in range(len(s)):
            s_map[s[right]] = s_map.get(s[right], 0)+1
            sub_str = s[left:right+1]
            while check(s_map, t_map):
                if len(s[left:right+1])<min_len:
                    ans = s[left:right+1]
                    min_len = len(ans)

                s_map[s[left]] -= 1

                if s_map[s[left]] == 0:
                    del s_map[s[left]]

                left += 1
            
        return ans