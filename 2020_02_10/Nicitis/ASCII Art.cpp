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

		// T에 해당하는 문자열을 한 줄씩 answer에 저장한다
		for (int j = 0; j < T.length(); j++)
		{
			// ASCII 코드로 변환하여 A부터 0, 1, 2, 3, 4,... 의 열 번호를 따온다.
			// A to Z에 해당하지 않을 경우 26번(? 문자) 할당)
			int column = (int)toupper(T[j]) - 65;
			if (column < 0 || column > 25)
				column = 26;

			// 해당하는 문자의 i번째 행을 저장한다
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