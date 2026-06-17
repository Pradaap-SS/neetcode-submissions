# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.ans=-float('inf')

        def solve(root):
            if root is None:
                return 0
            
            left=max(0,solve(root.left))
            right=max(0,solve(root.right))

            self.ans=max(self.ans, left+root.val+right)

            return root.val+max(left,right)

        solve(root)
        return self.ans