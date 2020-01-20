#include <string>
#include <vector>

using namespace std;

vector<int> solution(int n) {
    vector<int> answer(1,0);
    
    for(int i = 2; i <= n; i++)
    {
        vector<int> temp(answer);
        answer.push_back(0);
        
        for(int j = temp.size()-1; j >= 0; j--)
        {
            temp[j] == 1 ? answer.push_back(0) : answer.push_back(1);
        }
    }
    return answer;
}