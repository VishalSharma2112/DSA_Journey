class Solution:
    def finalPrices(self, prices: list[int]) -> list[int]:
        ans = [0]*len(prices)
        stack = []
        for i in range(len(prices)-1, -1, -1):
            while(len(stack)!=0 and prices[i]<stack[-1]):
                stack.pop()
            if len(stack)==0:
                ans[i] = prices[i]
            else:
                ans[i] = prices[i] - stack[-1]
            stack.append(prices[i])
        return ans