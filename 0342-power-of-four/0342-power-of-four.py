class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n==1:
            return True
        for i in range(2, 31, 2):
            if n == 1<<i:
                return True
        return False