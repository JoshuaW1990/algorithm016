class Solution:
    # def rotate(self, nums: List[int], k: int) -> None:
    def rotate(self, nums, k):
        """
        Do not return anything, modify nums in-place instead.
        """
        # double reverse
        n = len(nums)
        if n <= 1:
            return
        turns = k % n
        def reverseHelper(start, end):
            i = 0
            while i < int((end - start + 1)/2):
                nums[start + i], nums[end - i] = nums[end - i], nums[start + i]
                i += 1
            return

        reverseHelper(0, n-1)
        reverseHelper(0, turns-1)
        reverseHelper(turns, n-1)

solution = Solution()
# nums = [1,2,3,4]
# nums = [1,2,3,4,5,6,7]
nums = [1,2]
# k = 2
k = 3
solution.rotate(nums, k)
print(nums)
