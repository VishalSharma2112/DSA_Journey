class Solution {
public:
    int countPrimes(int n) {
        if(n==0 || n==1 || n==2){
            return 0;
        }
        int count = n-2;
        vector<int> arr(n-2, 1);
        
        for(int i=2 ; i <= sqrt(n) ; i++){
            for(int j = i*i ; j<n ; j+=i){
                if(arr[j-2] == 1){
                    arr[j-2] = 0;
                    count --;
                }
            }
        }
        return count;
        }
};