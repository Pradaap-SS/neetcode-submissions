class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {}  # key -> Node

        # Dummy nodes: left=LRU end, right=MRU end
        self.left  = Node(0, 0)   # LRU sentinel
        self.right = Node(0, 0)   # MRU sentinel
        self.left.next  = self.right
        self.right.prev = self.left
        

    # Remove node from its current position
    def remove(self, node):
        prev, nxt = node.prev, node.next
        prev.next = nxt
        nxt.prev  = prev

    # Insert node at MRU end (just before right sentinel)
    def insert(self, node):
        prev, nxt = self.right.prev, self.right
        prev.next = node
        nxt.prev  = node
        node.prev = prev
        node.next = nxt
        
    def get(self, key: int) -> int:
        if key in self.cache:
            node = self.cache[key]
            self.remove(node)    # remove from current position
            self.insert(node)    # re-insert at MRU end
            return node.val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])   # remove old node
        node = Node(key, value)
        self.cache[key] = node
        self.insert(node)                  # insert at MRU end

        if len(self.cache) > self.cap:
            # Evict LRU (node just after left sentinel)
            lru = self.left.next
            self.remove(lru)
            del self.cache[lru.key]