def solution(clothes):
    answer = 1
    clothesDic = {}
    for item in clothes:
        if item[1] not in clothesDic:
            clothesDic[item[1]] = 2
        else:
            clothesDic[item[1]] = clothesDic[item[1]] + 1
    counts = clothesDic.values()
    for count in counts:
        answer = answer * count
    return answer - 1


# 착용하지 않는 케이스까지 포함해서 계산한 다음 단 하나도 걸치지 않은 케이스 1개만 빼주면 간편하다. 
