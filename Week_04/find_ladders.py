class Solution(object):
    def findLadders(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: List[List[str]]
        """
        word_set = set(wordList)
        layer = set([beginWord])
        parent_map = dict()
        # build map
        while layer:
            word_set = word_set - layer
            next_layer = set()
            for word in layer:
                for index in range(len(word)):
                    for ch in 'abcdefghijklmnopqrstuvwxyz':
                        new_word = word[:index] + ch + word[index+1:]
                        if new_word not in word_set:
                            continue
                        if new_word in parent_map:
                            parent_map[new_word].append(word)
                        else:
                            parent_map[new_word] = [word]
                        next_layer.add(new_word)
            layer = next_layer
            if endWord in layer:
                break
        # build path
        result = []
        def dfs(path):
            if path[-1] == beginWord:
                result.append(path[::-1])
                return
            last_word = path[-1]
            if last_word not in parent_map:
                return
            for word in parent_map[last_word]:
                dfs(path + [word])
        dfs([endWord])
        return result

solution = Solution()
beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log","cog"]
print(solution.findLadders(beginWord, endWord, wordList))

