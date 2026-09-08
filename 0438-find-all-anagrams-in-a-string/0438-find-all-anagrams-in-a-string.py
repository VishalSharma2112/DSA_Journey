class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        window_len = len(p)
        alpha = {}
        left = 0
        ans = []
        test = {}

        for i in p:
            test[i] = test.get(i, 0)+1

        for right in range(len(s)):
            alpha[s[right]] = alpha.get(s[right], 0)+1

            if right-left+1 == window_len:
                if alpha == test:
                    ans.append(left)

                alpha[s[left]] -= 1

                if alpha[s[left]] == 0:
                    del alpha[s[left]]

                left += 1
        return ans
        