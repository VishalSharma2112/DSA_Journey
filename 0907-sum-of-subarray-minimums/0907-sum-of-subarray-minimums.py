class Solution:
    def sumSubarrayMins(self, arr: list[int]) -> int:
        PSE = [0]*len(arr)
        NSE = [0]*len(arr)
        mod = 10**9 + 7
        stack = []
        for i in range(len(arr)): # PSE
            while(len(stack)!=0 and arr[i] < arr[stack[-1]]):
                stack.pop()
            if len(stack) == 0:
                PSE[i] = -1
            else:
                PSE[i] = stack[-1]
            stack.append(i)
        stack = []
        for i in range(len(arr)-1, -1, -1): # NSE
            while(len(stack)!=0 and arr[i] <= arr[stack[-1]]):
                stack.pop()
            if len(stack) == 0:
                NSE[i] = len(arr)
            else:
                NSE[i] = stack[-1]
            stack.append(i)

        total = 0
        for i in range(len(arr)):
            left = i - PSE[i]
            right = NSE[i] - i
            total = (total + (right * left * arr[i])) % mod

        return total