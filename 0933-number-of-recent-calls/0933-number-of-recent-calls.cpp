class RecentCounter {
    queue<int> arr;
public:
    RecentCounter() {
        
    }
    
    int ping(int t) {
        arr.push(t);
        while(t-arr.front() > 3000){
            arr.pop();
        }
        return arr.size();
    }
};

/**
 * Your RecentCounter object will be instantiated and called as such:
 * RecentCounter* obj = new RecentCounter();
 * int param_1 = obj->arr(t);
 */