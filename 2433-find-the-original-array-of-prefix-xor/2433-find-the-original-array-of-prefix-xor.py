class Solution:
    def findArray(self, pref: List[int]) -> List[int]:
        XOR = 0
        ans = []
        for i in pref:
            ans.append(XOR^i)
            XOR = i
        return ans