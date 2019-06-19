class Solution:

    avail_numbers = {}
    flag = False

    def init(self):
        Solution.flag = True
        for number in range(1, 10001):
            for n in str(number):
                if n == '0':
                    break

                if number % int(n) != 0:
                    break
            else:
                Solution.avail_numbers[number] = True


    def selfDividingNumbers(self, left: int, right: int):

        result = []
        # init all case
        if not Solution.flag:
            self.init()

        for number in range(left, right + 1):
            if number in Solution.avail_numbers:
                result.append(number)

        return result
