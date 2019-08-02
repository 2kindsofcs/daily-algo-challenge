"""
LeetCode : 997. Find the Town Judge
problem : https://leetcode.com/problems/find-the-town-judge/
Solution:
아래의 조건이 충족되는지 확인하기 위해서 dict 자료구조를 이용한다.
- 주민들은 반드시 judge를 신뢰한다는 것을 보여줘야 한다. -> judge를 제외한 N-1명의 주민들이 judge를 신뢰하고 있어야 함
- judge는 그 누구도 신뢰하고 있지 않아야 한다.
"""

class Solution:
    def findJudge(self, N: int, trust) -> int:
        if N == 1:
            return 1

        # judge를 제외한 주민들의 신뢰를 보여줄 수 없을 경우 -1
        if len(trust) < N - 1:
            return -1

        judge = None
        judge_cnt = 0
        judge_cnt_dict = {}
        trust_dict = {}

        for case in trust:
            n, judge_n = case
            # 누가 누구를 신뢰하고 있는지
            trust_dict.setdefault(n, [])
            trust_dict[n].append(judge_n)

            # 누가 얼마나 많은 사람들의 신뢰를 받고 있는지
            judge_cnt_dict.setdefault(judge_n, 0)
            judge_cnt_dict[judge_n] += 1

            # 최다 신뢰자 = judge
            if judge_cnt < judge_cnt_dict[judge_n]:
                judge_cnt = judge_cnt_dict[judge_n]
                judge = judge_n

        # judge가 모든 주민의 신뢰를 받지 못하는 경우
        if N-1 != judge_cnt:
            return -1

        # judge가 다른 사람을 신뢰하고 있을 경우
        if judge in trust_dict:
            return -1
        return judge


s = Solution()
print(s.findJudge(1, []))  # 1
print(s.findJudge(2, [[1,2]]))  # 2
print(s.findJudge(3, [[1,3],[2,3]])) # 3
print(s.findJudge(3, [[1,3],[2,3],[3,1]])) # -1
print(s.findJudge(3, [[1,2],[2,3]])) # -1
print(s.findJudge(4, [[1,3],[1,4],[2,3],[2,4],[4,3]])) # 3

