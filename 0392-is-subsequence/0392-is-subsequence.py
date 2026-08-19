class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if s=="":
            return True
        n = len(t)
        i = 0
        j = 0
        while i<len(s) and j < n:
            if s[i] == t[j]:
                i+=1
            j+=1
        if i == len(s):
            return True
        else:
            return False