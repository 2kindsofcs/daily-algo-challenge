from collections import defaultdict

def solution(tickets):
    # tickets 훑으면서 출발지: [도착지1,도착지2...] 형태의 딕셔너리 만듦
    ticketDic = defaultdict(list)
    for start, dest in tickets:
        ticketDic[start].append(dest)
    for ticket in ticketDic:
        ticketDic[ticket].sort(reverse=True)
    
    path = []
    stack = ["ICN"]
    while stack:
        top = stack[-1]
        if top not in ticketDic or not ticketDic[top]:
            path.append(stack.pop())
        else:
            stack.append(ticketDic[top].pop())
    return path[::-1]
