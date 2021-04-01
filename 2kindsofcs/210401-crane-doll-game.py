def solution(board, moves):
    stack = []
    answer = 0 
    size = len(board)
    for i in moves:
        index = i - 1
        for line in board:
            if line[index] != 0:
                if stack and stack[-1] == line[index]:
                    stack.pop()
                    answer += 2
                else:
                    stack.append(line[index])
                line[index] = 0
                break
    return answer
  
  # https://programmers.co.kr/learn/courses/30/lessons/64061
  # 더 효율적인 방법이 있을 것도 같은데 :thinking face:
