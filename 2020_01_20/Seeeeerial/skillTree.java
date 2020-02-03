class Solution {
    public int solution(String skill, String[] skill_trees) {
        int answer = 0;
        int now = -1;       //스킬 순서의 지금 단계 없으면 -1
        int next = -1;        //다음 단계
        boolean success = true;     //가능한 스킬트리인가
        
        for(int i = 0; i < skill_trees.length; i++)
        {
            now = skill_trees[i].indexOf(skill.charAt(0));  //skill의 현재단계의 순서 저장
            success = true;
            for(int j = 1; j < skill.length(); j++)
            {
                next = skill_trees[i].indexOf(skill.charAt(j)); //skill의 다음 단계의 순서 저장
                /*지금단계의 글자는 없는데 다음단계는 있거나, 지금단계의 순서가 다음단계가 존재할때 그보다 뒤일때*/
                if((next != -1&&now == -1) || (now > next && next != -1))
                {
                    success = false;
                    break;
                }
                now = next;
            }
            if(success)
                answer++;
        }
        return answer;
    }
}