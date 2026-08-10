class Solution {
public:
    int sum_arr(vector<int>& array){
        int sum=0;
        for(int i=0 ; i<array.size();i++){
            sum+= array[i];
        }
        return sum;
    }
    int maximumWealth(vector<vector<int>>& accounts) {
        int MAX = -1;
        for (int i=0 ; i<accounts.size() ; i++){
            MAX = max(sum_arr(accounts[i]), MAX);
        }
        return MAX;
    }
};