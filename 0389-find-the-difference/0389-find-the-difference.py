class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        s_xor = 0
        t_xor = 0
        for i in s:
            s_xor ^= ord(i)
        for i in t:
            t_xor ^= ord(i)
        return chr(s_xor ^ t_xor)