class Solution {
public:
    string predictPartyVictory(string senate) {
        int n = senate.size()-1;
        queue<int> r_queue;
        queue<int> d_queue;
        for(int i=0 ; i<senate.size() ; i++){
            if(senate[i] == 'R'){
                r_queue.push(i);
            }else{
                d_queue.push(i);
            }
        }

        while(!r_queue.empty() && !d_queue.empty()){
            if(r_queue.front() < d_queue.front()){
                int temp = r_queue.front();
                r_queue.pop();
                d_queue.pop();
                r_queue.push(temp+n);
            }else{
                int temp = d_queue.front();
                d_queue.pop();
                r_queue.pop();
                d_queue.push(temp+n);
            }
        }
        if(r_queue.empty()){
            return "Dire";
        }else{
            return "Radiant";
        }
    }
};