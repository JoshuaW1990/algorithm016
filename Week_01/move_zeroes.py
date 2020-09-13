class Solution:
    # def moveZeroes(self, nums: List[int]) -> None:
    def moveZeroes(self, nums):
        """
        Do not return anything, modify nums in-place instead.
        """
        # two pointers
        slow = 0
        for fast in range(len(nums)):
            if nums[fast] != 0:
                nums[slow], nums[fast] = nums[fast], nums[slow]
                slow += 1


solution = Solution()
# nums = [0,1,0,3,12]
# nums = [4,2,4,0,0,3,0,5,1,0]
# nums = [0,0]
nums = [2,0,1]
solution.moveZeroes(nums)
print(nums)


