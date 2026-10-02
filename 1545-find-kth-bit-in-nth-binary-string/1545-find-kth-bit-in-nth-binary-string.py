class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        if n == 1:
            return "0"

        mid = 2 ** (n - 1)

        if k == mid:
            return "1"

        if k < mid:
            return str(self.findKthBit(n - 1, k))
        else:
            return str(1 - int(self.findKthBit(n - 1, 2**n % k)))