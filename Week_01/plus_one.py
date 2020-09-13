class Solution:
    # def plusOne(self, digits: List[int]) -> List[int]:
    def plusOne(self, digits):
        n = len(digits)
        if n == 0:
            return digits
        result = [0] * n
        tmp = 1
        index = n - 1
        while index >= 0:
            value = digits[index] + tmp
            tmp = int(value / 10)
            result[index] = value % 10
            index -= 1
        if tmp > 0:
            result = [tmp] + result
        return result

solution = Solution()
digits = [9,9]
print(solution.plusOne(digits))

