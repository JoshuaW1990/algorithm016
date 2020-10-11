class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        two layer of binary search
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        # 利用下表换算: O(log(M*N))
        # 计算效率不如两层二分
        height = len(matrix)
        if height <= 0:
            return False
        width = len(matrix[0])
        if width <= 0:
            return False
        left, right = 0, height * width - 1
        while left <= right:
            mid = int((left + right) / 2)
            num = matrix[int(mid / width)][mid % width]
            if num == target:
                return True
            elif num > target:
                right = mid - 1
            else:
                left = mid + 1
        return False

        # # 两层二分查找: O(logM) + O(logN)
        # height = len(matrix)
        # if height <= 0:
        #     return False
        # width = len(matrix[0])
        # if width <= 0:
        #     return False
        # top_row = 0
        # bottom_row = height - 1
        # final_row = -1
        # while top_row <= bottom_row:
        #     mid = int((top_row + bottom_row) / 2)
        #     if matrix[mid][0] <= target <= matrix[mid][width-1]:
        #         final_row = mid
        #         break
        #     elif target < matrix[mid][0]:
        #         bottom_row = mid - 1
        #     else:
        #         top_row = mid + 1
        # if final_row == -1:
        #     return False
        # left, right = 0, width-1
        # while left <= right:
        #     mid = int((left + right) / 2)
        #     if matrix[final_row][mid] == target:
        #         return True
        #     elif matrix[final_row][mid] < target:
        #         left = mid + 1
        #     else:
        #         right = mid - 1
        # return False

