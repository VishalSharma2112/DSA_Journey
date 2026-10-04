class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        xNew = 0
        temp = x
        while temp:
            xNew = (xNew*10) + (temp%10)
            temp //= 10
        if xNew == x:
            return True
        else:
            return False
