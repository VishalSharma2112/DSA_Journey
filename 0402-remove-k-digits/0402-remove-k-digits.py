class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        if k==len(num):
            return "0"
        stack = []
        for i in range(len(num)):
            while(len(stack)!=0 and int(num[i]) < int(stack[-1]) and k>0):
                k -= 1
                stack.pop()
            if len(stack)==0 and num[i]=='0':
                continue
            stack.append(num[i])
        ans = ''.join(stack)
        print(k, ans)
        if k >= len(ans):
            return "0"

        return ans[:len(ans)-k]

            