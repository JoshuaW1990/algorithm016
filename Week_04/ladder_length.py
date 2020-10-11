class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        BFS
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        word_set = set(wordList)
        layer = set([beginWord])
        cnt = 1
        while layer:
            next_layer = set()
            word_set = word_set - layer
            for word in layer:
                if word == endWord:
                    return cnt
                for index in range(len(word)):
                    for ch in 'abcdefghijklmnopqrstuvwxyz':
                        new_word = word[:index] + ch + word[index+1:]
                        if new_word in word_set:
                            next_layer.add(new_word)
            layer = next_layer
            cnt += 1
        return 0

solution = Solution()
# beginWord = "hit"
# endWord = "cog"
# wordList = ["hot","dot","dog","lot","log"]
beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log","cog"]
print(solution.ladderLength(beginWord, endWord, wordList))
