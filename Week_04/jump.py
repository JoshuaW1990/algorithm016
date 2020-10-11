class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # # BFS: 计算效率很低
        # n = len(nums)
        # if n <= 1:
        #     return 0
        # layer = [0]
        # cnt = 1
        # while layer:
        #     next_layer = set()
        #     layer.sort(reverse=True)
        #     for index in layer:
        #         num = nums[index]
        #         distance = num
        #         while distance > 0:
        #             right_most = distance + index
        #             if right_most >= n - 1:
        #                 return cnt
        #             next_layer.add(right_most)
        #             distance -= 1
        #     layer = list(next_layer)
        #     cnt += 1
        # return cnt

        # 贪心
        n = len(nums)
        max_pos, end, step = 0, 0, 0
        for i in range(n-1):
            max_pos = max(max_pos, nums[i] + i)
            if i == end:
                end = max_pos
                step += 1
        return step


solution = Solution()
nums = [2,3,1,1,4]
print(solution.jump(nums))
