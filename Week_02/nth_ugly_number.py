import heapq

class Solution:
    # def nthUglyNumber(self, n: int) -> int:
    def nthUglyNumber(self, n):
        """
        参考：https://leetcode-cn.com/problems/chou-shu-lcof/solution/li-yong-xiao-gen-dui-wan-mei-jie-jue-by-yanshaojia/
        这个方案里面的去重效率非常低，引入hashmap提高去重效率
        :param n:
        :return:
        """
        uglyNumber = [2,3,5]
        hp = [1]
        heapq.heapify(hp)
        cnt = 0
        uglySet = set(hp)
        while len(hp) > 0:
            result = heapq.heappop(hp)
            cnt += 1
            if cnt >= n:
                return result
            for num in uglyNumber:
                if num * result not in uglySet:
                    uglySet.add(num*result)
                    heapq.heappush(hp, num*result)
        return result

solution = Solution()
n = 10
print(solution.nthUglyNumber(n))

