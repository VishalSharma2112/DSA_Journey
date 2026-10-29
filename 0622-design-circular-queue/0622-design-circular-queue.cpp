class MyCircularQueue {
    vector<int> arr;
    int front = -1;
    int rear = -1;
    int size = 0;
    int capacity;

public:
    MyCircularQueue(int k) {
        arr = vector<int>(k, 0);
        capacity = k;
    }

    bool enQueue(int value) {
        if (isFull()) {
            return false;
        }

        if (isEmpty()) {
            front = 0;
            rear = 0;
        }
        else {
            rear = (rear + 1) % capacity;
        }

        arr[rear] = value;
        size++;

        return true;
    }

    bool deQueue() {
        if (isEmpty()) {
            return false;
        }

        if (size == 1) {
            front = -1;
            rear = -1;
        }
        else {
            front = (front + 1) % capacity;
        }

        size--;

        return true;
    }

    int Front() {
        if (isEmpty()) {
            return -1;
        }

        return arr[front];
    }

    int Rear() {
        if (isEmpty()) {
            return -1;
        }

        return arr[rear];
    }

    bool isEmpty() {
        return size == 0;
    }

    bool isFull() {
        return size == capacity;
    }
};