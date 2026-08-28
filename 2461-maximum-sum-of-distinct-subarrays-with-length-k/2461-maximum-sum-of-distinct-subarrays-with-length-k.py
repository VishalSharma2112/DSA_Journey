class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        left = 0
        max_sum = 0
        current_sum = 0
        count_set = {}

        for right in range(len(nums)):
            current_sum += nums[right]

            # Add number to frequency map
            count_set[nums[right]] = count_set.get(nums[right], 0) + 1

            if right - left + 1 == k:

                # All k elements are unique
                if len(count_set) == k:
                    max_sum = max(max_sum, current_sum)

                # Remove left element
                count_set[nums[left]] -= 1

                if count_set[nums[left]] == 0:
                    del count_set[nums[left]]

                current_sum -= nums[left]
                left += 1

        return(max_sum)