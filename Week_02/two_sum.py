class Solution:
    # def twoSum(self, nums: List[int], target: int) -> List[int]:
    def twoSum(self, nums, target):
        """
        1. 暴力搜索: O(N^2)
        2. hashMap: O(N)
        :param nums:
        :param target:
        :return:
        """
        hashMap = dict()
        for index, num in enumerate(nums):
            remain = target - num
            if remain in hashMap:
                return [hashMap[remain], index]
            else:
                hashMap[num] = index
        return [-1, -1]

