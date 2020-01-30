#include <iostream>
#include <stack>

using namespace std;

int solution(string s)
{
	stack<char> charStack;

	for (int i = 0; i < s.length(); i++)
	{
		if (charStack.size() > 0 && s[i] == charStack.top())
			charStack.pop();
		else
			charStack.push(s[i]);
	}

	return charStack.size() == 0;
}