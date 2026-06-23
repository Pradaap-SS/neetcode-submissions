'''class TreeNode:
    def __init__(self, val=0, left=None, right= None):
        self.val = val
        self.left = left
        self.right = right'''

class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        # root left right
        res = []

        def dfs(node, depth):
            if not node:
                return

            if depth == len(res):
                res.append(node.val)
            
            # Visit right first
            dfs(node.right, depth + 1)
            dfs(node.left, depth + 1)

        dfs(root, 0)
        return res

            
            



'''        while queue:
            rightmost = None

            for _ in range(len(queue)):
                node = queue.popleft()
                rightmost = node.val

                if node.left:
                    queue.append(node.left)

                if node.right:
                    queue.append(node.right)

            res.append(rightmost)

        return res'''

            



