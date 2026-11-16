# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        low = 1
        while low<=n:
            mid = (low+n)//2
            result = isBadVersion(mid)
            if result:
                n = mid-1
            else:
                low = mid+1
        return n+1