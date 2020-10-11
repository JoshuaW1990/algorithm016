class Solution(object):
    def lemonadeChange(self, bills):
        """
        :type bills: List[int]
        :rtype: bool
        """
        remain_cash = dict()
        remain_cash[5] = 0
        remain_cash[10] = 0
        remain_cash[20] = 0
        for bill in bills:
            if bill == 5:
                remain_cash[5] += 1
            elif bill == 10:
                if remain_cash[5] <= 0:
                    return False
                else:
                    remain_cash[5] -= 1
                remain_cash[10] += 1
            else:
                if remain_cash[10] > 0 and remain_cash[5] > 0:
                    remain_cash[10] -= 1
                    remain_cash[5] -= 1
                elif remain_cash[5] >= 3:
                    remain_cash[5] -= 3
                else:
                    return False
                remain_cash[20] += 1
        return True


solution = Solution()
bills = [5,5,5,10,20]
print(solution.lemonadeChange(bills))
