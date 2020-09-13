class Solution:
    # def twoSum(self, nums: List[int], target: int) -> List[int]:
    def twoSum(self, nums, target):
        hashMap = dict()
        for index, num in enumerate(nums):
            remain = target - num
            if remain in hashMap:
                return [hashMap[remain], index]
            else:
                hashMap[num] = index
        return [-1, -1]

solution = Solution()
nums = [1, 2, 3, 4]
target = 1
print(solution.twoSum(nums, target))
