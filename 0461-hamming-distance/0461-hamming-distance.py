class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        XOR = x^y
        count = 0
        while XOR:
            XOR = XOR&(XOR-1)
            count += 1
        return count