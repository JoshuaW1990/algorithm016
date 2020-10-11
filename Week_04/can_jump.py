class Solution(object):
    def canJump(self, nums):
        """
        greedy in reverse order
        https://leetcode-cn.com/problems/jump-game/solution/liang-chong-jie-jue-fang-shi-zui-hao-de-ji-bai-lia/
        :type nums: List[int]
        :rtype: bool
        """
        n = len(nums)
        if n <= 1:
            return True
        last = n - 1
        index = n - 2
        while index >= 0:
            if index + nums[index] >= last:
                last = index
            index -= 1
        return last == 0




solution = Solution()
# nums = [2,3,1,1,4]
# nums = [3,2,1,0,4]
# nums = [0]
# nums = [2,0,6,9,8,4,5,0,8,9,1,2,9,6,8,8,0,6,3,1,2,2,1,2,6,5,3,1,2,2,6,4,2,4,3,0,0,0,3,8,2,4,0,1,2,0,1,4,6,5,8,0,7,9,3,4,6,6,5,8,9,3,4,3,7,0,4,9,0,9,8,4,3,0,7,7,1,9,1,9,4,9,0,1,9,5,7,7,1,5,8,2,8,2,6,8,2,2,7,5,1,7,9,6]
# nums = [0,2,3]
# nums = [2,0,0]
nums = [2,3,1,1,4]
print(solution.canJump(nums))



