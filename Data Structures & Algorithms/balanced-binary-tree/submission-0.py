# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def dfs(node) -> int:
            if not node:
                return 0                          # height of empty tree = 0

            left  = dfs(node.left)
            if left == -1: return -1              # early exit: already unbalanced

            right = dfs(node.right)
            if right == -1: return -1             # early exit: already unbalanced

            if abs(left - right) > 1:
                return -1                         # this node is unbalanced

            return 1 + max(left, right)           # return height upward

        return dfs(root) != -1