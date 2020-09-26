# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
    def lowestCommonAncestor(self, root, p, q):
        """
        dfs
        https://leetcode-cn.com/problems/lowest-common-ancestor-of-a-binary-tree/solution/236-er-cha-shu-de-zui-jin-gong-gong-zu-xian-hou-xu/
        :param root:
        :param p:
        :param q:
        :return:
        """
        # root为None，返回None
        # root为p或者q，则返回root
        # 如果root的左右子树均无另一个节点（如root为p，子树无q）
        # 则最小公共祖先必然在root之上
        if root is None or root == p or root == q:
            return root
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        # 左子树为空或者找不到p和q
        if left is None:
            return right
        # 右子树为空或者找不到p和q
        if right is None:
            return left
        # 两个子树均有返回，说明左右子树均有p和q，那么root必然是最小公共祖先
        return root
