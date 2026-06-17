# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        stack = [(root, float('-inf'), float('inf'))]

        while stack:
            node, min_val, max_val = stack.pop()

            # Check current node against its valid range
            if not (min_val < node.val < max_val):
                return False

            # Push left child with updated upper bound
            if node.left:
                stack.append((node.left, min_val, node.val))

            # Push right child with updated lower bound
            if node.right:
                stack.append((node.right, node.val, max_val))

        return True