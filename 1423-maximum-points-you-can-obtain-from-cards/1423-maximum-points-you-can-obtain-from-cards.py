class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        if len(cardPoints)==k:
            return sum(cardPoints)
        total = sum(cardPoints)
        window_size = len(cardPoints)-k
        window_sum = 0
        left = 0
        ans = 0
        for right in range(len(cardPoints)):
            window_sum += cardPoints[right]

            if right-left+1 == window_size:
                ans = max(ans, total-window_sum)
                window_sum -= cardPoints[left]
                left += 1
        return(ans)