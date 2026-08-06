class Solution:
    def smallestNumber(self, n: int, t: int) -> int:
        product = 1
        for i in range(n, 101):
            if i//10 == 0:
                product = i
            else:
                product = (i%10)*(i//10)
            if product%t==0:
                return i