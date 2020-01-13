#include <string>
#include <vector>

using namespace std;

vector<int> solution(int n) {
    // solution(n) => solution(n-1) 채우고 중앙에 0, solution(n-1)을 뒤집은 걸 0과 1을 바꿔서 n번째부터 2n-1까지 채운다
    vector<int> answer;
    if(n == 1)
    {
        answer.push_back(0);
        return answer;
    }
    
    answer = solution(n-1);
    answer.push_back(0);
    
    int length = answer.size() - 2;
    
    for (int i = length; i >= 0 ; i--)
    {
        answer.push_back(answer[i] == 0 ? 1 : 0);
    }
    
    return answer;
}
