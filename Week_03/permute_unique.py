class Solution:
    # def permuteUnique(self, nums: List[int]) -> List[List[int]]:
    def permuteUnique(self, nums):
        """
        回溯，需要剪枝
        :param nums:
        :return:
        """
        result = []
        nums.sort()

        def dfs(path, remain_nums):
            if len(path) == len(nums):
                result.append(path[:])
                return
            for index, num in enumerate(remain_nums):
                if index > 0 and num == remain_nums[index-1]:
                    continue
                dfs(path+[num], remain_nums[:index]+remain_nums[index+1:])

        dfs([], nums)
        return result


solution = Solution()
nums = [1, 2, 1]
print(solution.permuteUnique(nums))

