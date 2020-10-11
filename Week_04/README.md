# 学习笔记

使用二分查找，寻找一个半有序数组 [4, 5, 6, 7, 0, 1, 2] 中间无序的地方:

## 思路
半有序数组的特点是绝大部分相邻元素为递增，只有无序点为递减状态
因此可以用二分法压缩搜索范围


## 代码
```python
def search(nums):
    n = len(nums)
    left, right = 0, n - 1
    # 不存在无序部分
    if nums[left] <= nums[right]:
        return -1
    while left <= right:
        mid = int((left + right) / 2)
        if nums[mid] > nums[mid+1]:
            return mid+1
        if nums[mid-1] > nums[mid]:
            return mid
        # 判断前半段是否有序
        if nums[0] <= nums[mid]:
            left = mid + 1
        else:
            right = mid - 1
    return -1
```