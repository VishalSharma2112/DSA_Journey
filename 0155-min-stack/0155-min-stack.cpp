class MinStack {
    stack<long long> s;
    long long mini = INT_MAX;

public:
    MinStack() {
    }

    void push(int value) {
        if (s.empty()) {
            mini = value;
            s.push(value);
            return;
        }

        if (value < mini) {
            s.push((2LL * value) - mini);
            mini = value;
        } else {
            s.push(value);
        }
    }

    void pop() {
        if (s.empty()) {
            return;
        }

        long long x = s.top();
        s.pop();

        if (x < mini) {
            mini = (2 * mini) - x;
        }
    }

    int top() {
        if (s.empty()) {
            return -1;
        }

        if (s.top() < mini) {
            return (int)mini;
        } else {
            return (int)s.top();
        }
    }

    int getMin() {
        return (int)mini;
    }
};