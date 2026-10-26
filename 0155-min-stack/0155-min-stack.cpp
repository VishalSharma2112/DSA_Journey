class MinStack {
    vector<pair<int, int>> s;
    int minimum = INT_MAX;

public:
    MinStack() {
    }
    
    void push(int value) {
        int minimum = value;

        if (!s.empty()) {
            minimum = min(value, s.back().second);
        }
        s.push_back({value, minimum});
        return;
    }
    
    void pop() {
        s.pop_back();
    }
    
    int top() {
        return s[s.size()-1].first;
    }
    
    int getMin() {
        return s[s.size()-1].second;
    }
};

/**
 * Your MinStack object will be instantiated and called as such:
 * MinStack* obj = new MinStack();
 * obj->push(value);
 * obj->pop();
 * int param_3 = obj->top();
 * int param_4 = obj->getMin();
 */