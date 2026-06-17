# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        stack = []
        curr = root
        while curr or stack:
            # Go all the way left
            while curr:
                stack.append(curr)
                curr = curr.left
            # Process current node
            curr = stack.pop()
            k -= 1

            if k == 0:
                return curr.val

            # Visit right subtree next
            curr = curr.right
        
        ''' elemIdx = 0
        res = -1
        def dfs(node):
            nonlocal elemIdx, k , res 

            if not node: return 0

            dfs(node.left)
            elemIdx += 1
            if (elemIdx == k):
                res = node.val
            dfs(node.right)
        
        dfs(root)
        return res '''


