class Solution {
public:
    vector<int> getMaximumXor(vector<int>& nums, int maximumBit) {
        int maxBit = (1 << maximumBit) - 1;
        vector<int> ans;
        vector<int> pxor(1, 0);

        // Build prefix XOR array
        for (int num : nums) {
            pxor.push_back(pxor.back() ^ num);
        }

        // Compute answers in reverse order
        for (int i = nums.size(); i >= 1; i--) {
            ans.push_back(pxor[i] ^ maxBit);
        }

        return ans;
    }
};