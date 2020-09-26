class Solution:
    # def permute(self, nums: List[int]) -> List[List[int]]:
    def permute(self, nums):
        """
        依然是迭代做路径枚举
        :param nums:
        :return:
        """
        result = []
        nums.sort()
        def dfs(path, remain_nums):
            if len(path) == len(nums):
                result.append([item for item in path])
                return
            for index, num in enumerate(remain_nums):
                dfs(path+[num], remain_nums[:index] + remain_nums[index+1:])
            return

        dfs([], nums)
        return result

solution = Solution()
nums = [1, 3, 4, 9, 7]
print(solution.permute(nums))
