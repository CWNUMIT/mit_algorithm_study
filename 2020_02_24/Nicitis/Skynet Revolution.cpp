#include <iostream>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

int main()
{
	int N; // the total number of nodes in the level, including the gateways
	int L; // the number of links
	int E; // the number of exit gateways
	cin >> N >> L >> E; cin.ignore();

	vector<vector<int>> connects(L, vector<int>(2, 0));
	vector<int> exits(E);

	for (int i = 0; i < L; i++) {
		cin >> connects[i][0] >> connects[i][1]; cin.ignore();
	}
	for (int i = 0; i < E; i++) {
		cin >> exits[i]; //cin.ignore();
	}

	while (1) {
		int SI;
		int index = 0;
		cin >> SI; cin.ignore();

		bool flag = false;

		// 시간복잡도 O(L * E)
		// SI와 EI가 이웃해 있을 때 Link를 자르고, 아니면 SI와 연결된 아무 선을 자른다.
		for (int i = 0; i < L; i++)
		{
			if (connects[i][0] == SI || connects[i][1] == SI)
			{
				// SI와 연결된 임의의 선을 고름
				index = (connects[i][0] == SI) ? connects[i][1] : connects[i][0];
				for (int j = 0; j < E; j++)
				{
					if (connects[i][0] == exits[j] || connects[i][1] == exits[j])
					{
						cout << connects[i][0] << " " << connects[i][1] << endl;
						flag = true;
						break;
					}
				}
			}
		}

		if (!flag)
			cout << SI << " " << index << endl;
	}
}