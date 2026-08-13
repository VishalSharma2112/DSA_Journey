#include <string>
#include <unordered_set>

class Solution {
public:
    string reverseVowels(string s) {
        int n = s.size();
        int i = 0;
        int j = n-1;
        unordered_set<char> vowels = {
            'a', 'e', 'i', 'o', 'u',
            'A', 'E', 'I', 'O', 'U'
        };
        while (j > i){
            if (vowels.count(s[i])==0){
                i ++;
            }
            else if (vowels.count(s[j])==0){
                j --;
            }
            else{
                swap(s[i], s[j]);
                i++;
                j--;
            }
        }
        return s;
        }
};