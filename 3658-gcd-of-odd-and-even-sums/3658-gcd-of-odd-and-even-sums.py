class Solution:
    def GCD(self, a: int, b: int) -> int:
        if b == 0:
            return a
        return self.GCD(b, a%b)
    def gcdOfOddEvenSums(self, n: int) -> int:
        odd_sum = n * n
        even_sum = n * (n + 1)
        return self.GCD(even_sum, odd_sum)
        