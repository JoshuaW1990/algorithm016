class Solution:
    # def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
    def groupAnagrams(self, strs):
        """
        1. 不排序hashmap：O(NK)
        2. 排序hashmap: O(NKlogK)
        :param strs:
        :return:
        """
        hashMap = dict()
        for word in strs:
            num_key = [0] * 26
            for ch in word:
                index = ord(ch) - ord('a')
                num_key[index] += 1
            key = "#".join([str(item) for item in num_key])
            if key in hashMap:
                hashMap[key].append(word)
            else:
                hashMap[key] = [word]
        return list(hashMap.values())

solution = Solution()
strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
print(solution.groupAnagrams(strs))