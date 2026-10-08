class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        if num == 1:
            return False
        Sum = 1
        for i in range(2, int(num**.5)+1):
            if num%i == 0:
                Sum += i+(num//i)
        return Sum==num