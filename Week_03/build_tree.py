# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
    def buildTree(self, preorder, inorder):
        """
        二叉树的遍历定义
        preorder: root在首位
        inorder: root在中间
        recursion
        use hashmap
        :param preorder:
        :param inorder:
        :return:
        """
        hashMap = dict()
        for index, num in enumerate(inorder):
            hashMap[num] = index

        def buildTreeHelper(preStart, preEnd, inStart, inEnd):
            n = preEnd - preStart
            if n <= 0:
                return None
            root = TreeNode(preorder[preStart])
            index = hashMap[preorder[preStart]]
            left_num = index - inStart
            root.left = buildTreeHelper(preStart+1, preStart + left_num + 1, inStart, inStart + left_num)
            root.right = buildTreeHelper(preStart + left_num + 1, preEnd, inStart + left_num + 1, inEnd)
            return root

        n = len(preorder)
        root = buildTreeHelper(0, n, 0, n)
        return root



solution = Solution()
preorder = [3,9,20,15,7]
inorder = [9,3,15,20,7]
print(solution.buildTree(preorder, inorder))