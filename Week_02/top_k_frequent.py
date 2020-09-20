import heapq
class Solution:
    # def topKFrequent(self, nums: List[int], k: int) -> List[int]:
    def topKFrequent(self, nums, k):
        """
        hashMap + heap: O(N) + O(NlogK) + O(KlogK) = O(NlogK)
        :param nums:
        :param k:
        :return:
        """
        hashMap = dict()
        for num in nums:
            if num in hashMap:
                hashMap[num] += 1
            else:
                hashMap[num] = 1
        hp = [(-value, key) for key, value in hashMap.items()]
        heapq.heapify(hp)
        result = []
        while len(result) < k and len(hp) > 0:
            freq, num = heapq.heappop(hp)
            result.append(num)
        return result

solution = Solution()
nums = [1,1,1,2,2,3]
k = 2
print(solution.topKFrequent(nums, k))


