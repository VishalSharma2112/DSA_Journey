class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        s_t = {}
        t_s = {}

        for i, j in zip(s, t):
            if i in s_t:
                if s_t[i] != j:
                    return False
            else:
                s_t[i] = j
            if j in t_s:
                if t_s[j] != i:
                    return False
            else:
                t_s[j] = i
        
        return True
