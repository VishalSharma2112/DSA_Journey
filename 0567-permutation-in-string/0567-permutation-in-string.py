class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        window_len = len(s1)
        left = 0
        per = {}
        test = {}
        for i in s1:
            test[i] = test.get(i, 0)+1

        for right in range(len(s2)):
            per[s2[right]] = per.get(s2[right], 0)+1

            if right-left+1 == window_len:
                if per == test:
                    return True
                
                per[s2[left]] -= 1

                if per[s2[left]] == 0:
                    del per[s2[left]]
                
                left += 1
        return False
                