# https://programmers.co.kr/learn/courses/30/lessons/49993

def solution(skill, skill_trees):
    # 스킬트리의 스킬이 있으면 배열에 넣음
    # 그 원소의 인덱스가 스킬에서의 인덱스와 동일한지 확인 
    answer = 0
    for userSkill in skill_trees:
        skillList = []
        for letter in userSkill:
            if letter in skill:
                skillList.append(letter)
        for i, letter in enumerate(skillList):
            if i != skill.index(letter):
                break
        else:
            answer += 1 
    return answer
    
# 10분. 
    
 
