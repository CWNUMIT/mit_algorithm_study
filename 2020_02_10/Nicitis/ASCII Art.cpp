#include <iostream>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

/**
 * Auto-generated code below aims at helping you parse
 * the standard input according to the problem statement.
 **/

int main()
{
	int L;
	cin >> L; cin.ignore();
	int H;
	cin >> H; cin.ignore();
	string T;
	getline(cin, T);

	vector<string> answer(H);

	for (int i = 0; i < H; i++) {
		string ROW;
		getline(cin, ROW);

		answer[i] = "";

		// T�� �ش��ϴ� ���ڿ��� �� �پ� answer�� �����Ѵ�
		for (int j = 0; j < T.length(); j++)
		{
			// ASCII �ڵ�� ��ȯ�Ͽ� A���� 0, 1, 2, 3, 4,... �� �� ��ȣ�� ���´�.
			// A to Z�� �ش����� ���� ��� 26��(? ����) �Ҵ�)
			int column = (int)toupper(T[j]) - 65;
			if (column < 0 || column > 25)
				column = 26;

			// �ش��ϴ� ������ i��° ���� �����Ѵ�
			answer[i] = answer[i] + ROW.substr(column * L, L);
		}
	}

	// Write an action using cout. DON'T FORGET THE "<< endl"
	// To debug: cerr << "Debug messages..." << endl;

	for (int i = 0; i < answer.size(); i++)
	{
		cout << answer[i] << endl;
	}
}