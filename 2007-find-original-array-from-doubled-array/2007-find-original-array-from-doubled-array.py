from typing import List

class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        if len(changed) % 2 != 0:
            return []

        count = {}

        for x in changed:
            count[x] = count.get(x, 0) + 1

        ans = []

        for x in sorted(changed):
            if count[x] == 0:
                continue

            if count.get(2 * x, 0) == 0:
                return []

            ans.append(x)

            count[x] -= 1
            count[2 * x] -= 1

        return ans