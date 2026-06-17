class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = None  # stores the complete word at the end node
        
class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        # Build the Trie
        root = TrieNode()
        for word in words:
            node = root
            for ch in word:
                if ch not in node.children:
                    node.children[ch] = TrieNode()
                node = node.children[ch]
            node.word = word

        rows, cols = len(board), len(board[0])
        result = []

        def dfs(r, c, node):
            ch = board[r][c]
            if ch not in node.children:
                return

            next_node = node.children[ch]

            if next_node.word:
                result.append(next_node.word)
                next_node.word = None  # avoid duplicates

            # Mark as visited
            board[r][c] = '#'

            for dr, dc in [(0,1),(0,-1),(1,0),(-1,0)]:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and board[nr][nc] != '#':
                    dfs(nr, nc, next_node)

            # Restore the cell
            board[r][c] = ch

            # Prune: remove leaf Trie nodes to optimize future searches
            if not next_node.children:
                del node.children[ch]

        for r in range(rows):
            for c in range(cols):
                dfs(r, c, root)

        return result