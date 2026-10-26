class MyStack {
    queue<int> s1;
public:
    MyStack() {
        
    }
    
    void push(int x) {
        if(s1.empty()){
            s1.push(x);
            return;
        }
        s1.push(x);
        for(int i=0 ; i<s1.size()-1 ; i++){
            s1.push(s1.front());
            s1.pop();
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