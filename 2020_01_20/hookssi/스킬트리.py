def IsValidSkillTree(skill_tree, skill):
    temp = [ skill_tree.get(skill_name, 26) for skill_name in skill ]
    if(temp == sorted(temp)):
        return 1
    else:
        return 0

def solution(skill, skill_trees):
    answer = 0
    for skill_tree in skill_trees:
        answer += IsValidSkillTree(dict(zip(skill_tree, range(len(skill_trees)))), skill)
    return answer