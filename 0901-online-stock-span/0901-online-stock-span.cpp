class StockSpanner {
    stack<pair<int, int>> s;
    int count = -1;
public:
    StockSpanner() {
        
    }
    
    int next(int price) {
        count ++;
        while(!s.empty() and s.top().first <= price){
            s.pop();
        }
        int ans = (s.empty()) ? count-(-1) : count - (s.top().second);
        s.push({price, count});
        return ans;
    }
};

/**
 * Your StockSpanner object will be instantiated and called as such:
 * StockSpanner* obj = new StockSpanner();
 * int param_1 = obj->next(price);
 */