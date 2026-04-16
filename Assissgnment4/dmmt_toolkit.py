class BSTNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


class BST:
    def __init__(self):
        self.root = None

    def insert(self, key):
        self.root = self._insert(self.root, key)

    def _insert(self, node, key):
        if not node:
            return BSTNode(key)
        if key < node.key:
            node.left = self._insert(node.left, key)
        else:
            node.right = self._insert(node.right, key)
        return node

    def search(self, key):
        return self._search(self.root, key)

    def _search(self, node, key):
        if not node:
            return False
        if node.key == key:
            return True
        if key < node.key:
            return self._search(node.left, key)
        return self._search(node.right, key)

    def delete(self, key):
        self.root = self._delete(self.root, key)

    def _delete(self, node, key):
        if not node:
            return node
        if key < node.key:
            node.left = self._delete(node.left, key)
        elif key > node.key:
            node.right = self._delete(node.right, key)
        else:
            if not node.left:
                return node.right
            elif not node.right:
                return node.left
            temp = self._min(node.right)
            node.key = temp.key
            node.right = self._delete(node.right, temp.key)
        return node

    def _min(self, node):
        while node.left:
            node = node.left
        return node

    def inorder(self):
        self._inorder(self.root)
        print()

    def _inorder(self, node):
        if node:
            self._inorder(node.left)
            print(node.key, end=" ")
            self._inorder(node.right)


class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, u, v, w):
        if u not in self.graph:
            self.graph[u] = []
        self.graph[u].append((v, w))

    def print_graph(self):
        for node in self.graph:
            print(node, "->", self.graph[node])

    def bfs(self, start):
        visited = set()
        queue = [start]
        visited.add(start)

        while queue:
            node = queue.pop(0)
            print(node, end=" ")
            for neigh, _ in self.graph.get(node, []):
                if neigh not in visited:
                    visited.add(neigh)
                    queue.append(neigh)
        print()

    def dfs(self, start):
        visited = set()
        self._dfs(start, visited)
        print()

    def _dfs(self, node, visited):
        visited.add(node)
        print(node, end=" ")
        for neigh, _ in self.graph.get(node, []):
            if neigh not in visited:
                self._dfs(neigh, visited)


class HashTable:
    def __init__(self, size=5):
        self.size = size
        self.table = [[] for _ in range(size)]

    def hash(self, key):
        return key % self.size

    def insert(self, key, value):
        index = self.hash(key)
        self.table[index].append((key, value))

    def get(self, key):
        index = self.hash(key)
        for k, v in self.table[index]:
            if k == key:
                return v
        return None

    def delete(self, key):
        index = self.hash(key)
        for i, (k, v) in enumerate(self.table[index]):
            if k == key:
                self.table[index].pop(i)
                return

    def display(self):
        for i in range(self.size):
            print(i, "->", self.table[i])


if __name__ == "__main__":

    print("BST Test")
    bst = BST()
    for x in [50, 30, 70, 20, 40, 60, 80]:
        bst.insert(x)

    print("Search 20:", bst.search(20))
    print("Search 90:", bst.search(90))

    print("Inorder:")
    bst.inorder()

    print("Delete leaf (20):")
    bst.delete(20)
    bst.inorder()

    print("Insert 65 and delete 60 (one child):")
    bst.insert(65)
    bst.delete(60)
    bst.inorder()

    print("Delete node with two children (30):")
    bst.delete(30)
    bst.inorder()

    print("\nGraph Test")
    g = Graph()
    edges = [
        ('A','B',2), ('A','C',4), ('B','D',7), ('B','E',3),
        ('C','E',1), ('D','F',5), ('E','D',2), ('E','F',6),
        ('C','F',8)
    ]
    for u,v,w in edges:
        g.add_edge(u,v,w)

    print("Adjacency List:")
    g.print_graph()

    print("BFS from A:")
    g.bfs('A')

    print("DFS from A:")
    g.dfs('A')

    print("\nHash Table Test")
    ht = HashTable(5)

    keys = [10, 15, 20, 7, 12]
    for k in keys:
        ht.insert(k, k*10)

    print("Hash Table:")
    ht.display()

    print("Get 10:", ht.get(10))
    print("Get 7:", ht.get(7))
    print("Get 12:", ht.get(12))

    print("Delete 15:")
    ht.delete(15)
    ht.display()