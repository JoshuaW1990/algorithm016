class Solution(object):
    def findMin(self, nums):
        """
        https://leetcode-cn.com/problems/find-minimum-in-rotated-sorted-array/solution/xun-zhao-xuan-zhuan-pai-lie-shu-zu-zhong-de-zui-xi/
        binary search
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        left, right = 0, n-1
        if nums[left] <= nums[right]:
            return nums[left]
        while left <= right:
            mid = int((left + right) / 2)
            if nums[mid] > nums[mid+1]:
                return nums[mid+1]
            if nums[mid-1] > nums[mid]:
                return nums[mid]
            if nums[0] <= nums[mid]:
                left = mid + 1
            else:
                right = mid - 1
        return -1

solution = Solution()
nums = [1, 2]
print(solution.findMin(nums))
