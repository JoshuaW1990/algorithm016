class Solution:
    # def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
    def merge(self, nums1, m, nums2, n):
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # three pointers
        ptr1 = m - 1
        ptr2 = n - 1
        ptr3 = m + n - 1
        while ptr2 >= 0 and ptr1 >= 0:
            num1 = nums1[ptr1]
            num2 = nums2[ptr2]
            if num1 > num2:
                nums1[ptr3] = nums1[ptr1]
                ptr1 -= 1
            else:
                nums1[ptr3] = nums2[ptr2]
                ptr2 -= 1
            ptr3 -= 1
        while ptr2 >= 0 and ptr1 < 0:
            nums1[ptr3] = nums2[ptr2]
            ptr3 -= 1
            ptr2 -= 1

solution = Solution()
# nums1 = [1, 2, 3, 0, 0]
# m = 3
# nums2 = [4, 5]
# n = 2
nums1 = [4, 5, 0, 0, 0]
m = 2
nums2 = [1, 2, 3]
n = 3
solution.merge(nums1, m, nums2, n)
print(nums1)

