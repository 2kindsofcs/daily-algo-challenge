class Solution {
public:
    int findContentChildren(vector<int>& g, vector<int>& s) {
        std::sort(g.begin(), g.end());
        std::sort(s.begin(), s.end());
        int count = 0;
        // cbegin, cend? 가리키고 있는 내용물 값이 변하지 않을 경우. 
        auto itG = g.cbegin();
        auto endG = g.cend();
        // 안 변할 것이고,  데이터형을 신경쓰지 않을 것이며, 데이터 복사는 원하지 않으며 읽기
        for (const auto& candy : s) {
            if (candy >= *itG) {
                count++;
                itG++;
                if (itG == endG) {
                    break;
                }
            } 
        }
        
        return count;
    }
};

// Runtime: 44 ms, faster than 49.13% of C++ online submissions for Assign Cookies.
// Memory Usage: 10.2 MB, less than 100.00% of C++ online submissions for Assign Cookies.
// 파이썬에서 이터레이터 사용해서 풀려고 했으나, 값을 가져오는 것과 다음 값을 가리키는 게 항상 동시에 일어나야 함.
// 원하는 대로 풀 수가 없어서 C++로 풀어보았다. 
