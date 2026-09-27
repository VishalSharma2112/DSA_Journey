class Solution {
public:
    string reverseParentheses(string s) {
        int n = s.size();

        stack<int> st;
        vector<int> pair(n);
        string ans;

        for (int i = 0; i < n; i++) {
            if (s[i] == '(') {
                st.push(i);
            }
            else if (s[i] == ')') {
                int j = st.top();
                st.pop();

                pair[i] = j;
                pair[j] = i;
            }
        }

        int i = 0;
        int direction = 1;

        while (i < n) {

            if (s[i] == '(' || s[i] == ')') {
                i = pair[i];
                direction = -direction;
            }
            else {
                ans += s[i];
            }

            i += direction;
        }

        return ans;
    }
};