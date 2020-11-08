class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        memo = dict()
        n = len(s)
        if n == 0:
            return 0
        for index, ch in enumerate(s):
            if index == 0:
                memo[index] = 1
                continue
            if ch != '0':
                memo[index] = memo[index-1]
            else:
                memo[index] = 0
            num = int(s[index-1:index+1])
            if 10 <= num <= 26:
                memo[index] += 1
            else:
                memo[index] += memo[index-2]
        return memo[n-1]


solution = Solution()
s = "101"
print(solution.numDecodings(s))