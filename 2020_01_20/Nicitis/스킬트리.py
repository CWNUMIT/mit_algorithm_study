"""
���ེų ������ ���Ե��� ���� ��ų -> ������ ���� ����
���ེų ������ ���Ե� -> ���� ������ ���;� �� ��ų�� �ƴϴ�(indexSkill�� ����) -> �Ұ����� ��ųƮ��
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