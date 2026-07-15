class Solution:
    def GCD(self, a: int, b: int) -> int:
        if b == 0:
            return a
        return self.GCD(b, a%b)
    def gcdOfOddEvenSums(self, n: int) -> int:
        odd_sum = 0
        even_sum = 0
        for i in range(1, 2*n+1):
            if i%2 == 0:
                even_sum += i
            else:
                odd_sum += i
        return self.GCD(even_sum, odd_sum)
        