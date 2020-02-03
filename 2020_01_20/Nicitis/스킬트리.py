"""
선행스킬 순서에 포함되지 않은 스킬 -> 순서와 관계 없다
선행스킬 순서에 포함됨 -> 지금 순서에 나와야 할 스킬이 아니다(indexSkill로 구별) -> 불가능한 스킬트리
"""
def solution(skill, skill_trees):
    answer = 0
    for tree in skill_trees:
        if is_valid_tree(skill, tree):
            answer += 1

    return answer

def is_valid_tree(skill, skill_tree):
    index_skill = 0
    for element in skill_tree:
        if element in skill:
            if element != skill[index_skill]:
                return False
            index_skill += 1
    return True