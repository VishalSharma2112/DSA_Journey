class Solution:
    def GCD(self, a: int, b: int) -> int:
        if b==0:
            return a
        return self.GCD(b, a%b)
    def findGCD(self, nums: List[int]) -> int:
        return self.GCD(min(nums), max(nums))