class Solution(object):
    def search(self, nums, target):
        """
        binary search
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        n = len(nums)
        def helper(left, right):
            if left > right:
                return -1
            mid = int((left + right) / 2)
            if nums[mid] == target:
                return mid
            if nums[left] <= nums[mid]:
                if nums[left] <= target <= nums[mid]:
                    return helper(left, mid-1)
                else:
                    return helper(mid+1, right)
            else:
                if nums[mid] <= target <= nums[right]:
                    return helper(mid+1, right)
                else:
                    return helper(left, mid-1)
        return helper(0, n-1)

solution = Solution()
nums = [4,5,6,7,0,1,2]
target = 0
print(solution.search(nums, target))
