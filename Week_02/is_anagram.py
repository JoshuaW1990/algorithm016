class Solution:
    # def isAnagram(self, s: str, t: str) -> bool:
    def isAnagram(self, s, t):
        """
        1. 暴力搜索: O(N^2)
        2. 排序比较: O(NlogN)
        3. hashmap: O(N)
        """
        if len(s) != len(t):
            return False
        hashMap = dict()
        for ch in s:
            if ch in hashMap:
                hashMap[ch] += 1
            else:
                hashMap[ch] = 1
        for ch in t:
            if ch not in hashMap or hashMap[ch] <= 0:
                return False
            else:
                hashMap[ch] -= 1
        return True
