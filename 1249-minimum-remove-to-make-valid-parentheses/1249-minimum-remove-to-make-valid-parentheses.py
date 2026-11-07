class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack = []
        for i in range(len(s)):
            if s[i] == '(':
                stack.append(['(', i])
            if s[i] == ')':
                if len(stack) != 0 and stack[-1][0] == '(':
                    stack.pop()
                    continue
                stack.append([')', i])

        ans = ""
        stack = stack[::-1]
        for i in range(len(s)):
            if len(stack)!=0 and i == stack[-1][1]:
                stack.pop()
                continue
            ans += s[i]

        return ans


