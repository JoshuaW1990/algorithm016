class Solution(object):
    def findContentChildren(self, g, s):
        """
        :type g: List[int]
        :type s: List[int]
        :rtype: int
        """
        g.sort()
        s.sort()
        p1, p2 = 0, 0
        while p1 < len(g) and p2 < len(s):
            if g[p1] <= s[p2]:
                p1 += 1
                p2 += 1
            else:
                p2 += 1
        return p1

solution = Solution()
g = [1,2]
s = [1, 1, 1]
print(solution.findContentChildren(g, s))