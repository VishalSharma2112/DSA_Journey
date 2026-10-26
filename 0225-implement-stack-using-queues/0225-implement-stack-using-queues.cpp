class MyStack {
    queue<int> s1;
    queue<int> s2;
public:
    MyStack() {
        
    }
    
    void push(int x) {
        if(s1.empty()){
            s1.push(x);
            return;
        }
        while(!s1.empty()){
            s2.push(s1.front());
            s1.pop();
        }
        s1.push(x);
        while(!s2.empty()){
            s1.push(s2.front());
            s2.pop();
        }
        return;
    }
    
    int pop() {
        int temp = s1.front();
        s1.pop();
        return temp;
    }
    
    int top() {
        return s1.front();
    }
    
    bool empty() {
        if(s1.empty()){
            return true;
        }else{
            return false;
        }
    }
};

/**
 * Your MyStack object will be instantiated and called as such:
 * MyStack* obj = new MyStack();
 * obj->push(x);
 * int param_2 = obj->pop();
 * int param_3 = obj->top();
 * bool param_4 = obj->empty();
 */