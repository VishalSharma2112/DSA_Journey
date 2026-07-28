class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        jewel = set()
        count = 0
        for i in jewels:
            if i not in jewel:
                jewel.add(i)
        for i in stones:
            if i in jewel:
                count += 1
        return count