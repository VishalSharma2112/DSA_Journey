class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if str1+str2 != str2+str1:
            return ""
        a = len(str1)
        b = len(str2)
        def gcd(a, b):
            if a == 0:
                return b
            return gcd(b%a, a)
        strGcd = gcd(a, b)
        return str1[:strGcd]