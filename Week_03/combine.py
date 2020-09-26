class Solution:
    # def combine(self, n: int, k: int) -> List[List[int]]:
    def combine(self, n, k):
        """
        用迭代解决路径枚举
        :param n:
        :param k:
        :return:
        """
        result = []

        def dfs(path, current_num):
            if len(path) == k:
                result.append([item for item in path])
                return
            if current_num > n:
                return
            for num in range(current_num, n+1):
                dfs(path + [num], num+1)
            return

        dfs([], 1)
        return result

solution = Solution()
n = 4
k = 2
print(solution.combine(n, k))

