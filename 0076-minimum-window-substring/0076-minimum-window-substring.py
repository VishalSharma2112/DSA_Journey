class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t:
            return ""

        t_map = {}
        s_map = {}

        for ch in t:
            t_map[ch] = t_map.get(ch, 0) + 1

        need = len(t_map)
        have = 0

        left = 0
        min_len = float('inf')
        ans = ""

        for right in range(len(s)):
            ch = s[right]
            s_map[ch] = s_map.get(ch, 0) + 1

            if ch in t_map and s_map[ch] == t_map[ch]:
                have += 1

            while have == need:
                window_len = right - left + 1

                if window_len < min_len:
                    min_len = window_len
                    ans = s[left:right + 1]

                left_ch = s[left]
                s_map[left_ch] -= 1

                if left_ch in t_map and s_map[left_ch] < t_map[left_ch]:
                    have -= 1

                left += 1

        return ans