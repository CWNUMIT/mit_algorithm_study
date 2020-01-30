#include <iostream>
#include <stack>

using namespace std;

int solution(string s)
{
	/*
	짝지어서 제거할 수 있는 문자열 = 뒤집어도 똑같은 문자열(팰린드롬)들로 구성
	(예외 : abccbkddka, 팰린드롬 안에 팰린드롬이 들어 있다...)
	앞뒤 대칭을 확인할 수 있는 방법은 바로, 스택을 이용해 지금까지 나온 문자들을 저장해서 제거하는 것!
	*/
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
