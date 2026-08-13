class Solution:
    def longestRepeating(self, s: str, queryCharacters: str, queryIndices: List[int]) -> List[int]:
        st = SegmentTree(s)
        res = []
        for i in range(len(queryIndices)):
            st.update(st.root, queryIndices[i], queryCharacters[i])
            res.append(st.query())
        return res

class SegmentTreeNode:
    def __init__(self, l, r):
        self.l = l
        self.r = r
        self.left_char = None
        self.right_char = None
        self.left_len = 0
        self.right_len = 0
        self.max_len = 0
        self.left_child = None
        self.right_child = None

class SegmentTree:
    def __init__(self, s):
        self.s = list(s)
        self.n = len(self.s)
        self.root = self.build(0, self.n - 1)

    def build(self, l, r):
        node = SegmentTreeNode(l, r)
        if l == r:
            node.left_char = node.right_char = self.s[l]
            node.left_len = node.right_len = node.max_len = 1
        else:
            mid = (l + r) // 2
            node.left_child = self.build(l, mid)
            node.right_child = self.build(mid + 1, r)
            self.merge(node)
        return node

    def merge(self, node):
        left = node.left_child
        right = node.right_child
        node.left_char = left.left_char
        node.right_char = right.right_char
        node.left_len = left.left_len
        node.right_len = right.right_len
        node.max_len = max(left.max_len, right.max_len)

        if left.right_char == right.left_char:
            if left.left_len == (left.r - left.l + 1):
                node.left_len += right.left_len
            if right.right_len == (right.r - right.l + 1):
                node.right_len += left.right_len
            node.max_len = max(node.max_len, left.right_len + right.left_len)

    def update(self, node, idx, char):
        if node.l == node.r:
            self.s[idx] = char
            node.left_char = node.right_char = char
            node.left_len = node.right_len = node.max_len = 1
        else:
            mid = (node.l + node.r) // 2
            if idx <= mid:
                self.update(node.left_child, idx, char)
            else:
                self.update(node.right_child, idx, char)
            self.merge(node)

    def query(self):
        return self.root.max_len