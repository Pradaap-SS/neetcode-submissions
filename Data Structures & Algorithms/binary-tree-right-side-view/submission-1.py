# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        res = []
        queue = deque([root])

        while queue:
            rightmost = None
            for _ in range(len(queue)):       # process entire level
                node = queue.popleft()
                rightmost = node.val          # keep overwriting → last = rightmost
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            res.append(rightmost)

        return res

'''
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = {}

        def dfs(node, depth):
            if not node:
                return
            res[depth] = node.val      # rightmost always overwrites at this depth
            dfs(node.left, depth + 1)
            dfs(node.right, depth + 1) # right visited last → wins at each depth

        dfs(root, 0)
        return [res[d] for d in range(len(res))]
'''