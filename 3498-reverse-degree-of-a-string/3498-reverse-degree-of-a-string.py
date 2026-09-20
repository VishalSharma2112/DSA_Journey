class Solution:
    def reverseDegree(self, s: str) -> int:
        ans = 0

        for index, i in enumerate(s):
            ans += (index+1)*abs(ord(i)%97-26)
        return(ans)