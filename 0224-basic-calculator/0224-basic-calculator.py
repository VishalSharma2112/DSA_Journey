
class Solution:
    def calculate(self, s: str) -> int:
        num = 0
        sign = 1
        stack = []
        ans = 0

        for i in range(len(s)):

            if s[i].isdigit():
                num = num * 10 + int(s[i])

            elif s[i] == '+':
                ans += num * sign
                num = 0
                sign = 1

            elif s[i] == '-':
                ans += num * sign
                num = 0
                sign = -1

            elif s[i] == '(':
                stack.append(ans)
                stack.append(sign)

                ans = 0
                num = 0
                sign = 1

            elif s[i] == ')':
                ans += num * sign
                num = 0

                ans *= stack.pop()
                ans += stack.pop()

        return ans + num * sign
