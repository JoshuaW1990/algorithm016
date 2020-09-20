# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # def inorderTraversal(self, root: TreeNode) -> List[int]:
    def inorderTraversal(self, root):
        """
        dfs算法
        1. 迭代
        2. 递归
        :param root:
        :return:
        """
        # 递归
        # 基于颜色标记法：https://leetcode-cn.com/problems/binary-tree-inorder-traversal/solution/yan-se-biao-ji-fa-yi-chong-tong-yong-qie-jian-ming/
        if root is None:
            return []
        result = []
        stack = [(1, root)]
        while len(stack):
            unVisit, node = stack.pop()
            if node is None:
                continue
            if unVisit == 1:
                stack.append((1, node.right))
                stack.append((0, node))
                stack.append((1, node.left))
            else:
                result.append(node.val)
        return result

        # # 迭代
        # result = []
        #
        # def dfs(node):
        #     if node is None:
        #         return
        #     dfs(node.left)
        #     result.append(node.val)
        #     dfs(node.right)
        #
        # dfs(root)
        # return result

