class Solution {
public:
    vector<int> maxSlidingWindow(vector<int>& nums, int k) {
        priority_queue<pair<int, int>> pq;
        vector<int> ans;

        int left = 0;

        for (int right = 0; right < nums.size(); right++) {

            pq.push({nums[right], right});

            if (right - left + 1 == k) {

                while (pq.top().second < left) {
                    pq.pop();
                }

                ans.push_back(pq.top().first);

                left++;
            }
        }

        return ans;
    }
};