class Solution:
    def removeDuplicates(self, s: str) -> str:
        if len(s) == 1:
            return s
        stack = []
        for i in s:
            if len(stack)==0:
                stack.append(i)
                continue
            if stack[-1] == i:
                stack.pop()
                continue
            stack.append(i)
        ans = ""
        for i in stack:
            ans += i
        return ans