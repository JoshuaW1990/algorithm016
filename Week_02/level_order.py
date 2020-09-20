"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""


class Solution:
    # def levelOrder(self, root: 'Node') -> List[List[int]]:
    def levelOrder(self, root):
        """
        BFS
        :param root:
        :return:
        """
        result = []
        queue = [(0, root)]
        while len(queue):
            depth, node = queue.pop(0)
            if node is None:
                continue
            while depth >= len(result):
                result.append([])
            result[depth].append(node.val)
            for ch in node.children:
                queue.append((depth+1, ch))
        return result
