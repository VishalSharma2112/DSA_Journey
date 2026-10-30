class RecentCounter {
    queue<int> arr;
    int size = 0;
public:
    RecentCounter() {
        
    }
    
    int ping(int t) {
        arr.push(t);
        size += 1;
        if(t-arr.front() <= 3000){
            return size;
        }
        while(t-arr.front() > 3000){
            arr.pop();
            size -= 1;
        }
        return size;
    }
};

/**
 * Your RecentCounter object will be instantiated and called as such:
 * RecentCounter* obj = new RecentCounter();
 * int param_1 = obj->arr(t);
 */