#include <string>
#include <vector>
#include <stack>

using namespace std;

int solution(int m, int n, vector<string> board)
{
	int answer = 0;
	vector<vector<bool>> check(m, vector<bool>(n, false));

	while (true)
	{
		bool flag = false;
		// 제거 대상 탐색(좌상단 블럭 검사)
		for (int i = 0; i < m - 1; i++)
		{
			for (int j = 0; j < n - 1; j++)
			{
				char c = board[i][j];
				if (c == ' ')
					continue;

				if (c == board[i + 1][j] && c == board[i][j + 1] && c == board[i + 1][j + 1])
				{
					flag = true;
					check[i][j] = check[i + 1][j] = check[i][j + 1] = check[i + 1][j + 1] = true;
				}
			}
		}

		if (!flag)
			break;

		stack<char> s;

		// 제거 및 스택을 이용한 정렬
		for (int j = 0; j < n; j++)
		{
			for (int i = 0; i < m; i++)
			{
				if (check[i][j])
				{
					check[i][j] = false;
					board[i][j] = ' ';
					answer++;
				}
				else
				{
					s.push(board[i][j]);
				}
			}

			for (int i = m - 1; i >= 0; i--)
			{
				if (!s.empty())
				{
					board[i][j] = s.top();
					s.pop();
				}
				else
					board[i][j] = ' ';
			}
		}
	}

	return answer;
}