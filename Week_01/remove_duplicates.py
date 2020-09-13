class Solution:
    # def removeDuplicates(self, nums: List[int]) -> int:
    # two pointers
    def removeDuplicates(self, nums):
        n = len(nums)
        if n <= 1:
            return n
        head = tail = 0
        while tail < n:
            if nums[head] == nums[tail]:
                tail += 1
            else:
                head += 1
                nums[head] = nums[tail]
        return head + 1


solution = Solution()
# nums = [1, 1, 2]
# nums = [0,0,1,1,1,2,2,3,3,4]
# nums = [1,1]
nums = [1,2]
print(solution.removeDuplicates(nums))
