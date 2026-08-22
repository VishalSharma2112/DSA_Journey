class Solution:
    def checkDivisibility(self, n: int) -> bool:
        original = n
        Sum = 0
        product = 1
        while n!=0:
            Sum += n%10
            product *= n%10
            n //= 10
        if original % (Sum + product) == 0:
            return True
        else:
            return False
