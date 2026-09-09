class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        freq = set()
        left = 0
        sub_str = ""
        ans = set()

        for right in range(len(s)):
            sub_str = s[left:right+1]

            if right-left+1 == 10:
                if sub_str in freq:
                    ans.add(sub_str)
                freq.add(sub_str)
                left += 1
        return list(ans)
                