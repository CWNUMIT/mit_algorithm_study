import java.util.Stack;

class Solution
{
    public int solution(String s)
    {
        int answer = 0;
        
        Stack<Character> stack = new Stack<>(); //스택정의

        for(int i = 0; i<s.length(); i++)
        {
            if(stack.isEmpty()) //스택이 비어있으면 일단 push
                stack.push(s.charAt(i));
            else if(stack.peek() == s.charAt(i))    //다음 순서랑 이전거랑 같으면 pop
                stack.pop();
            else    //다르면 일단 push
                stack.push(s.charAt(i));
        }
                    
        if(stack.isEmpty())     //다 하고 나서 비었으면 1
            answer = 1;
        else {answer = 0;}      //안비었으면 0

        return answer;
    }
}