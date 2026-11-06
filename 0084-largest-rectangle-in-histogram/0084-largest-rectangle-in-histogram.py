class Solution:
    def largestRectangleArea(self, heights: list[int]) -> int:
        def NSE(arr):
            stack = []
            NSE = [0]*len(arr)
            for i in range(len(arr)-1, -1, -1):
                while(len(stack)!=0 and arr[i] < arr[stack[-1]]):
                    stack.pop()
                if len(stack) == 0:
                    NSE[i] = len(arr)
                else:
                    NSE[i] = stack[-1]
                stack.append(i)
            return NSE


        def PSE(arr):
            stack = []
            PSE = [0]*len(arr)
            for i in range(len(arr)):
                while(len(stack)!=0 and arr[i] <= arr[stack[-1]]):
                    stack.pop()
                if len(stack) == 0:
                    PSE[i] = -1
                else:
                    PSE[i] = stack[-1]
                stack.append(i)
            return PSE


        NSE = NSE(heights)
        PSE = PSE(heights)
        area = -1

        for i in range(len(heights)):
            area = max(heights[i]*(NSE[i]-PSE[i]-1), area)


        return area