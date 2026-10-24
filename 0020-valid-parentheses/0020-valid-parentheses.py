class Solution:
    def isValid(self, s: str) -> bool:

        stack = []
        for i in s:
            if i == '(' or i == '[' or i == '{':
                stack.append(i)
            else:
                if not stack:
                    return False
                if i == ')':
                    if stack[-1] != '(':
                        return False
                elif i == ']':
                    if stack[-1] != '[':
                        return False
                else:
                    if stack[-1] != '{':
                        return False
                stack.pop()
        return len(stack)==0
            