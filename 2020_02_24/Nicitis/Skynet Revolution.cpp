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

		// �ð����⵵ O(L * E)
		// SI�� EI�� �̿��� ���� �� Link�� �ڸ���, �ƴϸ� SI�� ����� �ƹ� ���� �ڸ���.
		for (int i = 0; i < L; i++)
		{
			if (connects[i][0] == SI || connects[i][1] == SI)
			{
				// SI�� ����� ������ ���� ��
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