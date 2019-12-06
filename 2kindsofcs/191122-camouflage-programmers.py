import itertools
def solution(clothes):
    answer = 0
    clothesDic = {}
    for item in clothes:
        if item[1] not in clothesDic:
            clothesDic[item[1]] = 1
        else:
            clothesDic[item[1]] = clothesDic[item[1]] + 1
    categories = clothesDic.keys()
    categoryCount = len(categories)
    for i in range(1, categoryCount + 1):
        combiList = itertools.combinations(categories, i)
        for combi in combiList:
            result = 1
            for category in combi:
                result = result * clothesDic[category]
            answer = answer + result
    return answer  
    
 # 1번 테스트케이스를 시간 초과로 통과하지 못하고 있다. 
