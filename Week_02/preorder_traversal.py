# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # def preorderTraversal(self, root: TreeNode) -> List[int]:
    def preorderTraversal(self, root):
        """
        1. 迭代：略
        2. 递归：基于颜色标记法
        :param root:
        :return:
        """
        result = []
        stack = [(1, root)]
        while len(stack) > 0:
            unVisit, node = stack.pop()
            if node is None:
                continue
            if unVisit:
                stack.append((1, node.right))
                stack.append((1, node.left))
                stack.append((0, node))
            else:
                result.append(node.val)
        return result

