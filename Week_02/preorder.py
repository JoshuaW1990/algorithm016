"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    # def preorder(self, root: 'Node') -> List[int]:
    def preorder(self, root):
        if root is None:
            return []
        result = []
        stack = [root]
        while len(stack):
            node = stack.pop()
            result.append(node.val)
            for ch in node.children[::-1]:
                stack.append(ch)
        return result

